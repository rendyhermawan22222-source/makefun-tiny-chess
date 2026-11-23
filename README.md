# TinyChess v2 — 4 KB Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rendyhermawan22222-source/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rendyhermawan22222-source/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A stronger rewrite of our v1 entry ("TinyChess 4K") for make.fun bounty
`tiny-chess-01` (strongest chess engine in 4 KB of Python, $500, top 20 paid).

## What it is

`main.py` — **4,088 bytes**, plain ASCII, Python stdlib only. No compression,
no `exec`/`eval`, no files besides itself. It plays a full game through the
make.fun env (`POST /game`, `POST /move`), within the 10 s move limit and
the 1,800 s trial budget.

## How it plays

- 0x88 board, full move generation (castling, en passant, queen promotions).
- Negamax alpha-beta + quiescence, iterative deepening to depth 16 under a
  fixed 100,000-node budget per move (no wall clock, so live and replay agree).
- Transposition table on `(bytes(board), side, castling, en-passant)`,
  exact/lower-bound scores with mate-distance adjustment; MVV-LVA ordering.
- Incremental eval: material (100/320/330/500/900) + piece-square tables.

## Verification

Move generation fuzzed against python-chess: 0 divergences (120 games x
50 plies). Perft exact (startpos 20/400/8902, Kiwipete 48/2039/97862).
Local practice trials: trial-0 Elo **1,191**, trial-1 **1,279** (mean
1,235; v1 scored 1,099) — see BUILD-REPORT.md.

---

<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
