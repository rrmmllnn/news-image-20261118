# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rrmmllnn/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rrmmllnn/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-page newspaper front page summing up Wednesday 18 November 2026's world news in a single 1024×1024 image. The panels are drawn illustrations of the day's events; the headlines and captions state the day's reported facts.

## The six stories

1. **The Gulf war widens.** U.S. jets strike a missile site on Qeshm Island, Iran fires drones at U.S. bases in Kuwait and Bahrain, and a tanker burns in the Strait of Hormuz. The lead panel shows the strait at dusk: a burning tanker, the island's missile site, and the contrails over the Gulf.
2. **The Kerch Bridge falls.** The road arch collapses into the strait, cutting the land link to Crimea. The second panel frames the broken span from the waterline.
3. **Xi meets Putin in Shenzhen.** The two leaders meet ahead of the first three-way summit with Trump, the week's big diplomatic set piece. The panel is the handshake outside the Shenzhen hall.
4. **Democrats take the Senate 56–44.** Mary Peltola's win in Alaska hands them the chamber. The panel shows the Senate floor with the new tally board.
5. **Ebola passes 11,000 cases in DR Congo.** The outbreak keeps growing; the panel shows a treatment centre at night, lit by a single row of lamps.
6. **Voyager 1 reaches one light-day.** The probe is now a full light-day from Earth, the farthest any human object has ever been. The closing panel is the spacecraft alone against the dark, with Earth a pale dot.

The footer carries four more items in brief: the Gaza ceasefire warning, Cyclone Xavier, the Siberia plane crash, and Nvidia's record quarter.

## Method

The day's stories were picked from the morning briefings of 18 November, then laid out as a broadsheet: a masthead, a lead panel for the Gulf, two rows of story panels, and a footer strip. Each panel was drawn as an illustration rather than a photograph, so the page reads as one coherent front page instead of six unrelated pictures. The image was composed at 1024×1024 and kept under the 1 MiB cap. `main.py` copies the bundled `entry.png` to `/output/entry.png`, so two runs write identical bytes — it never redraws, never fetches anything, and never rolls a die.

## Run it

```sh
python3 main.py
```

Write the copy somewhere else, or just check the bundled image:

```sh
python3 main.py --output /tmp/entry.png
python3 main.py --verify
```

`--verify` prints the image's dimensions, size and SHA-256 and the six stories, then exits without writing anything.

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hwq4sqk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
