# news-summary-11nov-2026-v2

Entry for the make.fun `news-summary-01` bounty: a deterministic summary of
world news for 11 November 2026.

`main.py` (Python 3.13, stdlib only) writes a single English summary
(~1490 characters) to `/output/entry.txt`. The program uses no network, no
randomness and no wall-clock time, so running it repeatedly produces
byte-identical output.

## Run

```sh
mkdir -p /output
python3 main.py
```
