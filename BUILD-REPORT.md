# BUILD-REPORT — tiny-chess-01 entry-v2

`main.py` — **4,088 bytes** (cap 4,096), plain ASCII, stdlib only.

0x88 negamax alpha-beta + quiescence, iterative deepening to depth 16
under a fixed 100,000-node budget per move (no wall clock, so live and
replay agree). New vs v1 (1,099): transposition table on
`(bytes(board), side, castling, en-passant)` (exact/lower-bound scores);
MVV-LVA ordering + queen-promo bonus. Cut to fit: killers, check
extensions, bishop-pair bonus, rook/queen PSTs.

Bug found: first build scored trial-0 Elo 997 — fail-low nodes stored
as exact TT scores (a fail-low score is an upper bound). Fix: store
only when `bs > alpha_entry`. Trial-0 rose 997 → **1,191**.

Checks: fuzz vs python-chess 0 divergences (120 games x 50 plies);
perft exact (startpos 20/400/8902, Kiwipete 48/2039/97862); worst move
~6.6 s (< 10 s).

Practice trials (`python3 dev/run_trial.py <trial> <main.py>`):
trial-0 Elo **1,191** (2W/1D/3L, spare 210); trial-1 **1,279**
(2W/2D/2L, spare 155). Mean **1,235** — both clear the 1,154 floor.
