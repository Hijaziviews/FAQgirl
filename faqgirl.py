#!/usr/bin/env python3
"""
FAQgirl - Auto response to queries
A simple FAQ bot that provides automatic responses to frequently asked questions.
"""

import json
import difflib
from typing import Dict, List, Tuple, Optional

class FAQgirl:
    """Auto-response FAQ bot for business queries."""
    
    def __init__(self, faq_data_file: str = None):
        """Initialize FAQgirl with FAQ data."""
        self.faq_data = {}
        if faq_data_file:
            self.load_faq_data(faq_data_file)
        else:
            self.load_default_faq_data()
    
    def load_faq_data(self, filename: str) -> None:
        """Load FAQ data from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.faq_data = json.load(file)
        except FileNotFoundError:
            print(f"FAQ data file {filename} not found. Using default data.")
            self.load_default_faq_data()
        except json.JSONDecodeError:
            print(f"Invalid JSON in {filename}. Using default data.")
            self.load_default_faq_data()
    
    def load_default_faq_data(self) -> None:
        """Load default FAQ data for business scenarios."""
        self.faq_data = {
            "business_hours": {
                "keywords": ["hours", "open", "closed", "time", "schedule", "when"],
                "response": "Our business hours are Monday to Friday: 9:00 AM - 6:00 PM, Saturday: 10:00 AM - 4:00 PM. We are closed on Sundays and public holidays."
            },
            "contact_info": {
                "keywords": ["contact", "phone", "email", "address", "reach", "call"],
                "response": "You can reach us at:\n📞 Phone: +1 (555) 123-4567\n📧 Email: info@company.com\n📍 Address: 123 Business Street, City, State 12345"
            },
            "pricing": {
                "keywords": ["price", "cost", "fee", "charge", "payment", "expensive", "cheap"],
                "response": "Our pricing varies based on your specific needs. We offer competitive rates with flexible payment options. Please contact our sales team for a personalized quote tailored to your requirements."
            },
            "services": {
                "keywords": ["service", "offer", "provide", "do", "help", "support"],
                "response": "We offer a comprehensive range of services including:\n• Consulting and Strategy\n• Implementation Support\n• 24/7 Customer Service\n• Training and Documentation\n• Maintenance and Updates"
            },
            "delivery": {
                "keywords": ["delivery", "shipping", "timeline", "when", "how long", "receive"],
                "response": "Standard delivery takes 3-5 business days. Express delivery (1-2 business days) is available for an additional fee. Digital products are delivered instantly upon payment confirmation."
            },
            "refund_policy": {
                "keywords": ["refund", "return", "money back", "cancel", "satisfaction"],
                "response": "We offer a 30-day money-back guarantee on all our services. If you're not completely satisfied, contact us within 30 days for a full refund. Digital products have a 7-day refund policy."
            },
            "technical_support": {
                "keywords": ["technical", "support", "help", "problem", "issue", "bug", "error"],
                "response": "Our technical support team is available 24/7 to assist you. You can:\n• Submit a ticket through our support portal\n• Call our technical hotline: +1 (555) TECH-HELP\n• Chat with us live on our website\n• Email: support@company.com"
            },
            "partnership": {
                "keywords": ["partner", "collaboration", "work together", "joint", "alliance"],
                "response": "We're always interested in strategic partnerships! Please send your partnership proposal to partnerships@company.com or schedule a meeting with our business development team."
            }
        }
    
    def find_best_match(self, query: str) -> Tuple[Optional[str], float]:
        """Find the best matching FAQ category for a query."""
        query_lower = query.lower()
        best_match = None
        best_score = 0.0
        
        for category, data in self.faq_data.items():
            # Calculate keyword match score (any keyword found gives a base score)
            keyword_matches = sum(1 for keyword in data["keywords"] if keyword in query_lower)
            if keyword_matches > 0:
                keyword_score = 0.5 + (keyword_matches / len(data["keywords"]) * 0.3)
            else:
                keyword_score = 0.0
            
            # Calculate similarity score using difflib (more generous matching)
            similarity_scores = [difflib.SequenceMatcher(None, query_lower, keyword).ratio() 
                               for keyword in data["keywords"]]
            max_similarity = max(similarity_scores) if similarity_scores else 0
            
            # Also check if any keyword is a substring of the query
            substring_matches = sum(1 for keyword in data["keywords"] 
                                  if keyword in query_lower or any(word in keyword for word in query_lower.split()))
            substring_score = min(substring_matches / len(data["keywords"]), 0.4) if substring_matches > 0 else 0
            
            # Combined score with multiple factors
            combined_score = max(keyword_score, max_similarity * 0.8, substring_score)
            
            if combined_score > best_score:
                best_score = combined_score
                best_match = category
        
        return best_match, best_score
    
    def respond(self, query: str, confidence_threshold: float = 0.2) -> str:
        """Generate an automatic response to a query."""
        if not query.strip():
            return "Hello! I'm FAQgirl, your automated assistant. How can I help you today?"
        
        best_match, confidence = self.find_best_match(query)
        
        if best_match and confidence >= confidence_threshold:
            response = self.faq_data[best_match]["response"]
            confidence_indicator = "🟢" if confidence > 0.7 else "🟡" if confidence > 0.5 else "🟠"
            return f"{confidence_indicator} {response}\n\nℹ️ Confidence: {confidence:.1%}"
        else:
            return ("🔴 I'm sorry, I couldn't find a specific answer to your question. "
                   "Please contact our support team for personalized assistance:\n"
                   "📧 Email: support@company.com\n"
                   "📞 Phone: +1 (555) 123-4567\n\n"
                   "Or try rephrasing your question with keywords like: hours, contact, pricing, services, delivery, refund, support, or partnership.")
    
    def get_available_topics(self) -> List[str]:
        """Get list of available FAQ topics."""
        return list(self.faq_data.keys())
    
    def get_sample_questions(self) -> List[str]:
        """Get sample questions for demonstration."""
        return [
            "What are your business hours?",
            "How can I contact you?",
            "What are your prices?",
            "What services do you offer?",
            "How long does delivery take?",
            "What is your refund policy?",
            "I need technical support",
            "Are you interested in partnerships?"
        ]