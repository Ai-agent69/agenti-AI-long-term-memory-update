from longterm_memory import LongTermMemory


# ==========================================
# CREATE MEMORY SYSTEM
# ==========================================

memory_system = LongTermMemory()


# ==========================================
# CONVERSATION HISTORY
# ==========================================

conversation_history = []


# ==========================================
# START SYSTEM
# ==========================================

print("==========================================")
print("        AGENTIC MEMORY SYSTEM")
print("        LONG-TERM MEMORY")
print("==========================================")

print("\nSystem Ready!")
print("Type 'exit' to stop the conversation.")


# ==========================================
# CONVERSATION LOOP
# ==========================================

while True:

    user_input = input("\nYou: ").strip()


    # ======================================
    # EXIT
    # ======================================

    if user_input.lower() == "exit":

        print("\nConversation stopped.")

        memory_system.close()

        break


    # ======================================
    # EMPTY INPUT
    # ======================================

    if not user_input:

        print("Please enter a message.")

        continue


    # ======================================
    # PROCESS USER INPUT
    # ======================================

    result = memory_system.process(
        user_input,
        conversation_history
    )


    # ======================================
    # SAVE MESSAGE TO CONVERSATION HISTORY
    # ======================================

    conversation_history.append(
        user_input
    )