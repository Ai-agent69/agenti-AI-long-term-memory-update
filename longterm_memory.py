import sqlite3
from datetime import datetime

from context_analysis import ContextAnalyzer
from importance_analysis import ImportanceAnalyzer
from persistence_analysis import PersistenceAnalyzer


class LongTermMemory:

    def __init__(self):

        print("Loading Long-Term Memory...")

        self.context_analyzer = ContextAnalyzer()
        self.importance_analyzer = ImportanceAnalyzer()
        self.persistence_analyzer = PersistenceAnalyzer()

        self.connection = sqlite3.connect("memory.db")
        self.cursor = self.connection.cursor()

        self.create_table()

        print("Long-Term Memory Ready!")


    # ==========================================
    # CREATE DATABASE TABLE
    # ==========================================

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS long_term_memory (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                memory_text TEXT NOT NULL,

                memory_type TEXT NOT NULL,

                context_score REAL,

                importance_score REAL,

                importance_level TEXT,

                persistence_score REAL,

                persistence_level TEXT,

                created_at TEXT

            )
        """)

        self.connection.commit()


    # ==========================================
    # LONG-TERM CLASSIFIER
    # ==========================================

    def classify(
        self,
        context_result,
        importance_result,
        persistence_result
    ):

        context_score = context_result["context_score"]

        importance_score = importance_result["importance_score"]
        importance_level = importance_result["importance_level"]

        persistence_score = persistence_result["persistence_score"]
        persistence_level = persistence_result["persistence_level"]


        # Context condition
        if context_score < 0.50:
            return False


        # Importance conditions
        if importance_score < 0.60:
            return False

        if importance_level == "LOW":
            return False


        # Persistence conditions
        if persistence_score < 0.70:
            return False

        if persistence_level != "LONG_TERM":
            return False


        return True


    # ==========================================
    # STORE MEMORY
    # ==========================================

    def store_memory(
        self,
        user_input,
        context_result,
        importance_result,
        persistence_result
    ):

        self.cursor.execute("""
            INSERT INTO long_term_memory (

                memory_text,
                memory_type,
                context_score,
                importance_score,
                importance_level,
                persistence_score,
                persistence_level,
                created_at

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            user_input,

            "LONG_TERM",

            context_result["context_score"],

            importance_result["importance_score"],

            importance_result["importance_level"],

            persistence_result["persistence_score"],

            persistence_result["persistence_level"],

            datetime.now().isoformat()

        ))

        self.connection.commit()


    # ==========================================
    # PROCESS USER INPUT
    # ==========================================

    def process(
        self,
        user_input,
        conversation_history
    ):

        # --------------------------------------
        # 1. CONTEXT ANALYSIS
        # --------------------------------------

        context_result = self.context_analyzer.analyze(
            user_input,
            conversation_history
        )


        # --------------------------------------
        # 2. IMPORTANCE ANALYSIS
        # --------------------------------------

        importance_result = self.importance_analyzer.analyze(
            user_input
        )


        # --------------------------------------
        # 3. PERSISTENCE ANALYSIS
        # --------------------------------------

        persistence_result = self.persistence_analyzer.analyze(
            user_input
        )


        # --------------------------------------
        # 4. LONG-TERM CLASSIFICATION
        # --------------------------------------

        is_long_term = self.classify(
            context_result,
            importance_result,
            persistence_result
        )


        # ======================================
        # DISPLAY RESULTS
        # ======================================

        print("\n======================================")
        print("          MEMORY ANALYSIS")
        print("======================================")


        print("\nUser Input:")
        print(user_input)


        print("\n--- Context Analysis ---")

        print(
            "Context Score:",
            round(
                context_result["context_score"],
                3
            )
        )


        print("\n--- Importance Analysis ---")

        print(
            "Importance Score:",
            round(
                importance_result["importance_score"],
                3
            )
        )

        print(
            "Importance Level:",
            importance_result["importance_level"]
        )


        print("\n--- Persistence Analysis ---")

        print(
            "Persistence Score:",
            round(
                persistence_result["persistence_score"],
                3
            )
        )

        print(
            "Persistence Level:",
            persistence_result["persistence_level"]
        )


        # ======================================
        # CLASSIFICATION RESULT
        # ======================================

        print("\n--- Long-Term Classifier ---")


        if is_long_term:

            print("Is LONG_TERM: YES")


            self.store_memory(
                user_input,
                context_result,
                importance_result,
                persistence_result
            )


            print("Memory Stored: YES")
            print("Memory Type: LONG_TERM")
            print("Database: SQLite")


        else:

            print("Is LONG_TERM: NO")
            print("Memory Stored: NO")


        print("\n======================================")


        return {
            "user_input": user_input,
            "context": context_result,
            "importance": importance_result,
            "persistence": persistence_result,
            "is_long_term": is_long_term
        }


    # ==========================================
    # CLOSE DATABASE
    # ==========================================

    def close(self):

        self.connection.close()