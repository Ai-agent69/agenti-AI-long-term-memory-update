class ImportanceAnalyzer:

    def analyze(self, user_input):

        text = user_input.lower()

        # Information that is usually important to remember
        high_importance_keywords = [

            # Identity
            "my name",
            "i am",
            "i'm",
            "myself",
            "name is",
            "i like it",
          

            # Preferences
            "my favorite",
            "favorite",
            "i like",
            "i love",
            "i prefer",
            "i dislike",
            "i hate",

            # Goals
            "my goal",
            "goal",
            "my dream",
            "dream",
            "i want to become",
            "i want to be",
            "i plan to",
            "plan",
            "ambition",

            # Education
            "i study",
            "i am studying",
            "studying",
            "my college",
            "my university",
            "my course",
            "my degree",
            "my branch",
            "my subject",
            "i am prepearing for",
            "i know about it"

            # Career
            "my job",
            "my work",
            "my career",
            "my profession",
            "my company",
            "my internship",
            "my experience",

            # Skills
            "my skill",
            "my skills",
            "i know",
            "i can",
            "i learned",
            "i have experience",

            # Projects
            "my project",
            "my projects",
            "i am working on",
            "working on",
            "my research",
            "my thesis",

            # Personal preferences
            "my hobby",
            "my hobbies",
            "my interest",
            "my interests",
            "i prefer",
            "i usually",
            "my gole",
            "my scope"

            # Explicit memory requests
            "remember",
            "remember that",
            "don't forget",
            "do not forget",
            "keep this in mind",
            "save this",
            "store this",

            # Personal information
            "my birthday",
            "my location",
            "my city",
            "my country",
            "my language",
            "my email",
            "my address"
        ]

        # Information that is usually temporary
        low_importance_keywords = [

            "eating",
            "eat",
            "food",
            "drinking",
            "drink",
            "having lunch",
            "having dinner",
            "breakfast",
            "lunch",
            "dinner",

            "today",
            "tonight",
            "this morning",
            "this evening",
            "right now",
            "currently",
            "at the moment",

            "going to",
            "going out",
            "went to",
            "came from",

            "weather",
            "raining",
            "rain",
            "sunny",
            "cloudy",
            "hot",
            "cold",

            "temporary",
            "for now",
            "just now",
            "recently"
        ]

        score = 0.50

        # High importance
        for keyword in high_importance_keywords:

            if keyword in text:

                score += 0.35
                break

        # Temporary information
        for keyword in low_importance_keywords:

            if keyword in text:

                score -= 0.35
                break

        score = max(0.0, min(score, 1.0))

        # Importance level
        if score >= 0.70:

            level = "HIGH"

        elif score >= 0.40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {

            "importance_score": score,

            "importance_level": level

        }