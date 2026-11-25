# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/ajidasidiq/battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/ajidasidiq/battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab): one line of at most 200 characters — the phone battery's final message to the charger it waited for all day.

## The entry

> waited all day for you and now you want 100% in twenty minutes? i'm not a microwave. i'm a battery with boundaries and 2% left, so this is goodbye. the power bank can have you.

176 characters. The joke turns on the last line: after a day of waiting, the battery doesn't beg for a charge — it dumps the charger for the power bank. Spite, not sentiment.

## How it works

`main.py` writes that single line to `/output/entry.txt` and gate-checks it first: UTF-8 text, 1–200 characters, not only whitespace, a single line, and it verifies the bytes on disk match the entry exactly.

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
