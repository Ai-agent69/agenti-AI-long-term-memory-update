class ContextAnalyzer:

    def analyze(self, user_input, conversation_history):

        text = user_input.lower()

        # Words/phrases that usually refer to existing context
        context_keywords = [
            "this",
            "that",
            "it",
            "these",
            "those",
            "above",
            "previous",
            "earlier",
            "before",
            "mentioned",
            "said",
            "discussed",
            "as i said",
            "as mentioned",
            "same",
            "again",
            "continue",
            "continuing",
            "previously",
            "already",
            "also",
            "about",
            "related",
            "regarding",
            "project",
            "topic",
            "problem",
            "question",
            "answer",
            "slow",
            "fast",
            "come",
            "go",
            "GO"
        ]

        score = 0.50
        relevant_context = []

        # Check current message against previous conversation
        for message in conversation_history:

            previous_words = set(message.lower().split())
            current_words = set(text.split())

            common_words = previous_words.intersection(current_words)

            # Ignore very small/common matches
            useful_words = [
                word for word in common_words
                if len(word) > 3
            ]

            if len(useful_words) >= 2:

                relevance_score = min(
                    0.50 + len(useful_words) * 0.10,
                    1.0
                )

                relevant_context.append({
                    "score": relevance_score,
                    "message": message
                })

        # Keyword-based context detection
        for keyword in context_keywords:

            if keyword in text:
                score += 0.05

        score = min(score, 1.0)

        return {
            "context_score": score,
            "relevant_context": relevant_context
        }