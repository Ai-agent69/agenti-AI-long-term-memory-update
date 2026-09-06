class PersistenceAnalyzer:

    def analyze(self, user_input):

        text = user_input.lower()

        # Information that can remain useful for a long time
        long_term_keywords = [

            # Identity
            "my name",
            "i am",
            "i'm",
            "myself",
            "name is",
            "i like it"

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
            "my knowledge",

            # Projects
            "my project",
            "my projects",
            "i am working on",
            "working on",
            "my research",
            "my thesis",

            # Personal information
            "my hobby",
            "my hobbies",
            "my interest",
            "my interests",
            "my language",
            "my city",
            "my country",

            # Preferences
            "i usually",
            "i always",
            "i prefer",
            "i normally",

            # Explicit memory
            "remember",
            "remember that",
            "don't forget",
            "do not forget",
            "keep this in mind",
            "save this",
            "store this",

            # Future plans
            "future",
            "long term",
            "long-term",
            "career goal",
            "life goal"
        ]

        # Information that is normally temporary
        temporary_keywords = [

            # Food/activity
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

            # Time
            "today",
            "tonight",
            "yesterday",
            "tomorrow",
            "this morning",
            "this evening",
            "right now",
            "currently",
            "at the moment",
            "just now",

            # Temporary activities
            "going to",
            "going out",
            "went to",
            "came from",
            "watching",
            "playing",
            "sleeping",
            "studying today",

            # Weather
            "weather",
            "raining",
            "rain",
            "sunny",
            "cloudy",
            "storm",
            "hot",
            "cold",

            # Temporary state
            "busy",
            "tired",
            "hungry",
            "thirsty",
            "sleepy",
            "bored",
            "waiting",

            # Temporary location
            "at home",
            "at college",
            "at school",
            "at work",
            "outside",

            # Temporary events
            "meeting today",
            "class today",
            "exam today",
            "test today",
            "event today",

            "for now",
            "temporarily",
            "temporary"
        ]

        long_term_found = False
        temporary_found = False

        # Check long-term keywords
        for keyword in long_term_keywords:

            if keyword in text:

                long_term_found = True
                break

        # Check temporary keywords
        for keyword in temporary_keywords:

            if keyword in text:

                temporary_found = True
                break

        # ==========================================
        # SCORE CALCULATION
        # ==========================================

        if long_term_found and not temporary_found:

            score = 0.90

        elif long_term_found and temporary_found:

            score = 0.70

        elif temporary_found:

            score = 0.20

        else:

            score = 0.40


        # ==========================================
        # PERSISTENCE LEVEL
        # ==========================================

        if score >= 0.70:

            level = "LONG_TERM"

        else:

            level = "SHORT_TERM"


        return {

            "persistence_score": score,

            "persistence_level": level

        }