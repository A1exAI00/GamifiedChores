# GamifiedChores

## How to use

To show chores in `filename` (default file - `config.yaml`)

```bash
python3 chore.py show [filename]
```

To generate template with from configuration (default file - `config.yaml`):

```bash
python3 chore.py generate-template [filename]
```

## TODO

- Add command to distribute chores if type `АУК` as an auction (everyone gets 1000 points at the start, iteratively go through every chore, whoever bids the least - gets the chore); distribute chores of type `ОБЯЗ` randomly between whoever has the least amount of chores after the auction (so that everybody has approx. equal number of chores); output as `.yaml` file
- Add to `config.yaml` "bonus points" for doing bonus chores and "punish points" for not doing `ОБЯЗ` and `АУК` chores
