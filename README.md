# TinyChess 4K

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rendyhermawan22222-source/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rendyhermawan22222-source/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original 0x88-board chess engine in 4,087 bytes of plain Python: negamax alpha-beta with quiescence, iterative deepening to a fixed 100,000-node budget, incremental piece-square evaluation, full move generation (castling, en passant, queen promotions). Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, 500 USDC prize pool. Practice trials: 1,099 Elo, 1W-2D-3L per 6-game trial, no timeouts or illegal moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:PORT python3 main.py
```

The engine plays through the make.fun trial env (see the competition kit).

---

<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
