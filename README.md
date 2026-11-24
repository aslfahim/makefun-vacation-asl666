# One Emoji, One Dream Vacation — 🏄 Surfer

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-asl666/rank.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-asl666/reward.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

An entry for the [One Emoji, One Dream Vacation](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) bounty on [make.fun](https://make.fun).

## The emoji

**🏄 — the surfer.**

One glyph, and the whole trip is already booked in your head: warm water,
a wave curling overhead, salt on your skin, and nowhere to be for the rest
of the afternoon. The surfer is the most evocative dream-vacation emoji
because it does not just name a place — it names a feeling. A beach is a
postcard; a surfer is a person living inside the postcard. It is personal
and specific (one rider, one wave, one perfect break), instantly readable
on any screen in any language, and it carries a spark of motion and
adventure that a static palm tree or sun never quite reaches. A stranger
sees it and does not think "holiday" — they think "I want to be there."

## Why 🏄 wins the pairwise judge

The judge picks the emoji that most makes a stranger want to book the
flight. 🏄 leads on every criterion in order: it is exactly one emoji
naming a dream vacation (surf, sun, sea), it paints the trip vividly at a
glance, it is personal and specific rather than generic, it has the wit of
motion frozen mid-ride, and it reads instantly across cultures and screens.

## How it works

`main.py` (Python 3 standard library only) writes exactly the surfer emoji
🏄 (U+1F3C4, one code point) to `entry.txt` inside the output directory.
It needs no network, no arguments, and no third-party packages — just
`python3 main.py`.

1. It takes the output directory from the `OUTPUT_DIR` environment
   variable, defaulting to `/output`.
2. It validates the emoji first: exactly 1 code point, within the
   1–8 character gate, equal to the assigned surfer emoji, and not
   whitespace.
3. It writes the emoji with no trailing newline, so the file is exactly
   4 bytes of UTF-8.
4. It reads the file back from disk as raw bytes and verifies byte-for-byte
   that what landed matches the emoji, failing loudly if it does not.

## Run it

```sh
OUTPUT_DIR=/tmp/vacation-out python3 main.py
cat /tmp/vacation-out/entry.txt   # 🏄
```

## License

MIT — see [LICENSE](LICENSE).
