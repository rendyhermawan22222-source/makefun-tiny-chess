# BUILD-REPORT — tiny-chess-01 entry-v2

**Deliverable:** `entry-v2/main.py` — **4,088 bytes** (cap 4,096; 8 spare).

## Approach

0x88 negamax alpha-beta + quiescence, iterative deepening to depth 16
under a fixed 100,000-node budget per move (no wall clock, so live and
replay agree). Incremental eval: material 100/320/330/500/900 + PSTs
(pawn, knight, bishop, king; rooks/queens reuse the pawn table).

New vs v1 (1,099): transposition table on `(bytes(board), side, castling,
en-passant)` with exact/lower-bound scores; MVV-LVA ordering + queen-promo bonus. Cut to fit: killers, check
extensions, bishop-pair bonus, rook/queen PSTs.

## Bug found

First build scored trial-0 Elo 997: fail-low nodes were stored as
**exact** TT scores, but a fail-low score is an upper bound, so the
engine trusted phantom evaluations and blundered into mates. Fix:
store only when `bs > alpha_entry`. Trial-0 rose 997 → **1,191**.

## Checks

Fuzz vs python-chess: **0 divergences** (120 games x 50 plies). Perft
exact: 20/400/8902, Kiwipete 48/2039/97862. Worst move ~6.6 s (< 10 s).

## Practice trials (local kit, 6 games)

`python3 dev/run_trial.py <trial> ~/workspace/makefun/tiny-chess/entry-v2/main.py`

| trial | Elo | W/D/L | spare |
| trial-0 fixed | **1,191** | 2/1/3 | 210 |
| trial-1 fixed | **1,279** | 2/2/2 | 155 |

## Verdict

Mean of fixed trials: **1,235** (v1: 1,099). Both clear the 1,154 floor
and the 1,170 target. (6-game trials are noisy.)
