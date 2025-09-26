#!/usr/bin/env python3
"""
FAQgirl Interactive Demo
Allows business persons to test FAQgirl with their own queries.
"""

from faqgirl import FAQgirl
import sys

def print_welcome():
    """Print welcome message."""
    print("=" * 80)
    print("🤖 Welcome to FAQgirl Interactive Demo!")
    print("=" * 80)
    print()
    print("This demo allows you to test how FAQgirl responds to your questions.")
    print("Perfect for business persons to see the auto-response capabilities!")
    print()
    print("💡 Tips:")
    print("  • Try asking about: hours, contact, pricing, services, delivery, refunds")
    print("  • Use natural language - FAQgirl understands variations")
    print("  • Type 'help' to see sample questions")
    print("  • Type 'topics' to see available FAQ categories")
    print("  • Type 'quit' or 'exit' to end the demo")
    print()
    print("-" * 80)
    print()

def print_help(faq_bot: FAQgirl):
    """Print help information."""
    print("📚 Available FAQ Topics:")
    topics = faq_bot.get_available_topics()
    for topic in topics:
        print(f"  • {topic.replace('_', ' ').title()}")
    print()
    
    print("💡 Sample Questions:")
    sample_questions = faq_bot.get_sample_questions()
    for question in sample_questions:
        print(f"  • {question}")
    print()

def main():
    """Run the interactive FAQgirl demo."""
    print_welcome()
    
    # Initialize FAQgirl
    faq_bot = FAQgirl()
    
    print("🤖 FAQgirl is ready! Ask me anything about our business.")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("👤 Your Question: ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🤖 Thank you for trying FAQgirl! Goodbye! 👋")
                break
            elif user_input.lower() == 'help':
                print()
                print_help(faq_bot)
                continue
            elif user_input.lower() == 'topics':
                print("\n📚 Available FAQ Topics:")
                topics = faq_bot.get_available_topics()
                for topic in topics:
                    print(f"  • {topic.replace('_', ' ').title()}")
                print()
                continue
            elif user_input.lower() == 'clear':
                # Clear screen (works on most terminals)
                print("\033[2J\033[H")
                print_welcome()
                continue
            
            # Get response from FAQgirl
            print()
            print("🤖 FAQgirl Response:")
            response = faq_bot.respond(user_input)
            print(response)
            print()
            print("-" * 80)
            print()
            
        except KeyboardInterrupt:
            print("\n\n🤖 Demo interrupted. Thank you for trying FAQgirl! 👋")
            break
        except EOFError:
            print("\n\n🤖 Demo ended. Thank you for trying FAQgirl! 👋")
            break

if __name__ == "__main__":
    main()