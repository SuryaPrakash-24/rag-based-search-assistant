import sys
from dotenv import load_dotenv
from agent import get_rag_agent

# Load environment variables
load_dotenv(override=True)


def main():
    print("Initializing RAG Agent...")
    try:
        agent = get_rag_agent()
    except Exception as e:
        print(f"Error initializing agent: {e}")
        sys.exit(1)

    print("\n--- RAG Search Assistant Ready ---")
    print("Ask any question (or type 'exit' or 'quit' to end):\n")

    while True:
        try:
            user_input = input("Ask something: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            response = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )

            # Print the agent's final message output
            final_message = response["messages"][-1].content
            print(f"\n{final_message}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
