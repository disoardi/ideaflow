#!/usr/bin/env python3
"""
Check quali idee necessitano review.
Usato da GitHub Action per reminder.
"""

import re
from pathlib import Path
from datetime import datetime, timedelta

def parse_tracker(content):
    """Parse tracker and extract ideas"""
    ideas = []
    
    for line in content.split('\n'):
        if line.startswith('|') and not line.startswith('| ID'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5:
                ideas.append({
                    'id': parts[1],
                    'title': parts[2],
                    'status': parts[3],
                    'date': parts[4],
                    'notes': parts[5] if len(parts) > 5 else ''
                })
    
    return ideas

def check_review_needed(ideas):
    """Identify ideas needing review"""
    needs_review = []
    
    for idea in ideas:
        # Captured da >7 giorni
        if '🟠 Captured' in idea['status']:
            needs_review.append({
                'idea': idea,
                'reason': 'Captured da >7 giorni - Elaborare o scartare'
            })
        
        # In Progress da >30 giorni
        if '🟡 In Progress' in idea['status']:
            needs_review.append({
                'idea': idea,
                'reason': 'In Progress da tempo - Verificare blocchi'
            })
        
        # On Hold - check se time to review
        if '🔴 On Hold' in idea['status']:
            needs_review.append({
                'idea': idea,
                'reason': 'On Hold - Tempo di revisitare?'
            })
    
    return needs_review

def generate_summary(needs_review):
    """Generate summary for issue"""
    if not needs_review:
        return "✅ Nessuna idea richiede review questa settimana!"
    
    summary = f"Ci sono **{len(needs_review)}** idee che richiedono attenzione:\n\n"
    
    for item in needs_review:
        idea = item['idea']
        summary += f"### {idea['id']}: {idea['title']}\n"
        summary += f"- **Status:** {idea['status']}\n"
        summary += f"- **Reason:** {item['reason']}\n\n"
    
    return summary

def main():
    tracker_path = Path('ideas/idea-tracker.md')
    content = tracker_path.read_text(encoding='utf-8')
    
    ideas = parse_tracker(content)
    needs_review = check_review_needed(ideas)
    summary = generate_summary(needs_review)
    
    # Output for GitHub Action
    print(f"::set-output name=needs_review::{len(needs_review) > 0}")
    print(f"::set-output name=summary::{summary}")

if __name__ == '__main__':
    main()