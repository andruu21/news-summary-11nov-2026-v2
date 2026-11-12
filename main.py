"""Deterministic summary of world news for 11 November 2026."""

SUMMARY = (
    "War and diplomacy set the agenda on 11 November. In Zaporizhzhia, mayor Regina Kharchenko "
    "described a city living in constant fear of Russian attacks, even as NATO's deputy supreme "
    "allied commander endorsed Ukraine's strikes on Russian diesel infrastructure and US-convened "
    "talks began in Abu Dhabi over Europe's postwar security settlement. Russia's ambassador to "
    "Washington, Alexander Darchiev, died at 66; Moscow separately barred four French figures in "
    "retaliation for the expulsion of RT France chief Xenia Fedorova. Europe filled its streets: "
    "Spain held its first nationwide general strike since 2012 — 120,000 marched in Madrid over "
    "housing costs, with clashes in Barcelona — while Portugal shut every one of its roughly "
    "8,000 schools ahead of Storm Charles, the first such closure in living memory. France marked "
    "the armistice's 108th anniversary, Macron at the Arc de Triomphe, Le Pen and Melenchon at "
    "symbolic venues as the presidential election looms. Brussels proposed a Digital Fairness Act "
    "to end subscription traps, addictive design and hidden fees. Business briefs: SpaceX signed "
    "a EUR60M solar-cell deal with Germany's Singulus; Portugal's Vangest will build Saab Gripen "
    "parts; and hotter-than-forecast US inflation cooled Europe's tech rally. Elsewhere, Trinidad "
    "and Tobago's top court overturned the island's gay sex ban, French journalist Christophe "
    "Gleizes spent his 500th day in an Algerian prison, and EU leaders mostly skipped the COP31 "
    "leaders' summit opening."
)


def main() -> None:
    import os
    os.makedirs("/output", exist_ok=True)
    text = SUMMARY.strip()
    assert 1 <= len(text) <= 2000, len(text)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
