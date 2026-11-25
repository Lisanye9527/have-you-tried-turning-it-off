[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Lisanye9527/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Lisanye9527/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

# Have You Tried Turning It Off?

An entry for the make.fun bounty "Have You Tried Turning It Off?".

The entry is a one-line joke about the world's most famous piece of
tech-support advice: it works, the caller confirms it worked, and the
script simply ends — because there never was a page two. The program
in this repository (`main.py`, Python 3, standard library only) holds
that line as a constant, validates it against the bounty gate (UTF-8
text, 1–199 characters, a single line, not only whitespace), writes it
to `entry.txt`, and reads the file back to confirm the bytes match.

The entry text:

> Have you tried turning it off and on again? …You have? Then we're done here — that was the entire script. They never wrote a page two; I'm as lost as you are.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

When `MAKEFUN_OUTPUT_DIR` is unset, the program writes to `/output`,
matching the grader container.

## License

Licensed under the MIT License.
