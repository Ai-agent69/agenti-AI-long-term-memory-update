import sqlite3

db = sqlite3.connect("memory.db")

records = db.execute("""
    SELECT
        id,
        memory_text,
        memory_type,
        context_score,
        importance_score,
        importance_level,
        persistence_score,
        persistence_level,
        created_at
    FROM long_term_memory
""").fetchall()

print("\n===== STORED LONG-TERM MEMORIES =====")

for record in records:
    print("\nID:", record[0])
    print("Memory:", record[1])
    print("Type:", record[2])
    print("Context Score:", record[3])
    print("Importance Score:", record[4])
    print("Importance Level:", record[5])
    print("Persistence Score:", record[6])
    print("Persistence Level:", record[7])
    print("Created:", record[8])

db.close()