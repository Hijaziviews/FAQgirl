#!/usr/bin/env python3
"""
FAQgirl Demo Script
Demonstrates how FAQgirl automatically responds to business queries.
"""

from faqgirl import FAQgirl
import time

def print_separator():
    """Print a visual separator."""
    print("=" * 80)

def print_header():
    """Print demo header."""
    print_separator()
    print("🤖 FAQgirl - Auto Response Demo")
    print("Demonstrating automatic responses to business queries")
    print_separator()
    print()

def demo_interaction(faq_bot: FAQgirl, query: str):
    """Demonstrate a single FAQ interaction."""
    print(f"👤 Customer Query: {query}")
    print()
    
    # Simulate thinking time
    print("🤖 FAQgirl is processing your query...")
    time.sleep(0.5)
    
    response = faq_bot.respond(query)
    print(f"🤖 FAQgirl Response:")
    print(response)
    print()
    print("-" * 80)
    print()

def run_demo():
    """Run the complete FAQgirl demonstration."""
    print_header()
    
    # Initialize FAQgirl
    faq_bot = FAQgirl()
    
    # Demo scenarios with various types of business queries
    demo_queries = [
        # Direct questions
        "What are your business hours?",
        "How can I contact your company?",
        "What are your prices?",
        
        # Variations and natural language
        "When are you open?",
        "I need to reach someone at your company",
        "How much does it cost?",
        
        # More complex queries
        "I'm having technical issues with your service",
        "What kind of services do you provide?",
        "How long will it take to receive my order?",
        
        # Edge cases
        "Do you offer refunds if I'm not satisfied?",
        "Are you looking for business partners?",
        "Hello",  # Greeting
        "",       # Empty query
        "xyz123"  # Nonsensical query
    ]
    
    print("📋 Running demonstration with various business queries...\n")
    
    for i, query in enumerate(demo_queries, 1):
        print(f"Example {i}:")
        demo_interaction(faq_bot, query)
    
    # Show available topics
    print_separator()
    print("📚 Available FAQ Topics:")
    topics = faq_bot.get_available_topics()
    for topic in topics:
        print(f"  • {topic.replace('_', ' ').title()}")
    print()
    
    # Show sample questions
    print("💡 Sample Questions You Can Ask:")
    sample_questions = faq_bot.get_sample_questions()
    for question in sample_questions:
        print(f"  • {question}")
    print()
    
    print_separator()
    print("✅ Demo completed! FAQgirl successfully handled various business queries.")
    print("🎯 Business Value:")
    print("  • Instant 24/7 customer support")
    print("  • Consistent responses to common questions")
    print("  • Reduces support team workload")
    print("  • Improves customer satisfaction")
    print("  • Easy to customize and expand")
    print_separator()

if __name__ == "__main__":
    run_demo()