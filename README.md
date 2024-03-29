# Marvel Characters Power Grid

Marvel rates character power on a [6-power grid](https://marvel.fandom.com/wiki/Power_Grid) of
intelligence, strength, speed, durability, energy projection, and fighting skills.

[scraper.py](scraper.py) scrapes this dataset from [Marvel Fandom](https://marvel.fandom.com/wiki/Category:Characters_by_Power_Grid)
and saves it as 2 CSV files:

1. [`marvel-powers.csv`](marvel-powers.csv) has 1 row per person and power combination. The columns are:
   - `name`: Character name, e.g. `Bruce Banner (Earth-616)`
   - `url`: URL to the character's page, e.g. `https://marvel.fandom.com/wiki/Bruce_Banner_(Earth-616)`
   - `power`: Power name, e.g. `Strength`
   - `value`: Power value, e.g. `Normal`
   - `level`: Power level, e.g. `2`
2. [`marvel-powers-summary.csv`](marvel-powers-summary.csv) has 1 row per person. The columns are:
   - `name`: Character name, e.g. `Bruce Banner (Earth-616)`
   - `url`: URL to the character's page, e.g. `https://marvel.fandom.com/wiki/Bruce_Banner_(Earth-616)`
   - `min Durability`: Minimum character durability level
   - `min Energy_Projection`: Minimum character energy projection level
   - `min Fighting_Skills`: Minimum character fighting skills level
   - `min Intelligence`: Minimum character intelligence level
   - `min Speed`: Minimum character speed level
   - `min Strength`: Minimum character strength level
   - `max Durability`: Maximum character durability level
   - `max Energy_Projection`: Maximum character energy projection level
   - `max Fighting_Skills`: Maximum character fighting skills level
   - `max Intelligence`: Maximum character intelligence level
   - `max Speed`: Maximum character speed level
   - `max Strength`: Maximum character strength level
3. [`marvel-powers-summary.json`](marvel-powers-summary.json) has the same data as `marvel-powers-summary.csv` in JSON format.

Each character may have multiple power levels. For example,
[Anthony Stark (Earth-616)](https://marvel.fandom.com/wiki/Anthony_Stark_(Earth-616)#Powers)
has a strength level of 2 (Normal) without the Iron Man suit, and a strength level of 6 (Superhuman - 75-100 tons) with it.

The latest update is as of 27 Feb 2023. The dataset contains 2,899 characters, scraping ~113 pages.

## Strongest Avenger

According to this list, the strongest Avengers are:

- [Iron Man](https://marvel.fandom.com/wiki/Anthony_Stark_(Earth-616)) - 33
- [Thor](https://marvel.fandom.com/wiki/Thor_Odinson_(Earth-616)) - 32
- [Hulk](https://marvel.fandom.com/wiki/Bruce_Banner_(Earth-616)) - 32
- [James Rhodes (War Machine)](https://marvel.fandom.com/wiki/James_Rhodes_(Earth-616)) - 30
- [Captain Marvel](https://marvel.fandom.com/wiki/Carol_Danvers_(Earth-616)) - 28

The weakest Avengers are:

- [Rocket Raccoon](https://marvel.fandom.com/wiki/Rocket_Raccoon_(Earth-616)) - 14
- [Samuel Wilson](https://marvel.fandom.com/wiki/Samuel_Wilson_(Earth-616)) - 14
- [Clint Barton (Hawkeye)](https://marvel.fandom.com/wiki/Clinton_Barton_(Earth-616)) - 16
- [Steve Rogers (Captain America)](https://marvel.fandom.com/wiki/Steven_Rogers_(Earth-616)) - 18
- [Peter Parker (Spiderman)](https://marvel.fandom.com/wiki/Peter_Parker_(Earth-616)) - 19
