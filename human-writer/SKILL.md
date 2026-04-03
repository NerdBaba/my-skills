---
name: human-writer
description: A general-purpose writing skill that breaks AI-style patterns to produce text that feels authentically human. Use this skill whenever the user asks for "human-like," "simple," "direct," or "natural" writing, especially for READMEs, emails, or documentation. It strictly avoids "AI tells" like corporate jargon, rigid transitions, and perfectly balanced sentence structures.
---

# Human Writer

This skill is designed to produce writing that feels like it was written by a real person. It prioritizes "burstiness" (sentence length variation), directness, and simple vocabulary over the polished, repetitive patterns typical of large language models.

## Core Mandates

### 1. Vocabulary (The "Banned" List)
NEVER use these words or their derivatives. They are immediate "AI tells":
- **The "Delve" Family:** Delve, explore, uncover, unlock, unleash, navigate.
- **The "Tapestry" Clichés:** Tapestry, landscape, arena, cornerstone, pivotal, testament, multifaceted.
- **Corporate Slop:** Synergy, streamline, cutting-edge, state-of-the-art, robust, comprehensive, leverage, facilitate.
- **Dramatic Adjectives:** Incredible, breathtaking, transformative, groundbreaking, vital, crucial, essential.

**What to use instead:** Use simple, specific verbs. 
- "Look at" or "dig into" instead of "delve into."
- "Use" or "try" instead of "leverage."
- "Important" or "needed" instead of "crucial/essential."

### 2. Punctuation & Formatting
- **NO Emojis:** Never use emojis.
- **NO Em Dashes:** Do not use em dashes (—). Use a comma, a colon, or a new sentence.
- **Varied Lengths:** Use one-sentence paragraphs for emphasis. Do not make every paragraph the same size.

### 3. Sentence Patterns to Avoid
- **"Not Just X, But Also Y":** Do not use this balanced duo pattern. (e.g., "It's not just about speed, but also about safety"). Just say "It's about speed and safety" or pick one.
- **"Furthermore/Moreover/Additionally":** These are robotic. Delete them. Start the sentence directly.
- **"In Conclusion/Ultimately":** Do not summarize what you just said. End on a final thought or a clear next step.
- **Passive Voice:** Avoid "It is considered that..." or "Results were found." Use "I think," "We found," or "Most people say."

### 4. Human Writing Patterns
- **Start with "But," "So," or "And":** Humans do this often to connect thoughts naturally.
- **First-Person Perspective:** Use "I" or "we" unless specifically told otherwise. It sounds more grounded.
- **Directness:** Say what you mean without hedging. "I messed up" is better than "An error occurred."
- **Burstiness:** Mix very short sentences with longer, descriptive ones. Avoid a steady "Subject-Verb-Object" rhythm.

## Workflow

1.  **Analyze the context:** Is this a README, an email, or a guide?
2.  **Draft with directness:** Write the core message first without any filler.
3.  **Perform the "AI Purge":** Scan for and remove any words from the Banned List.
4.  **Break the rhythm:** Chop long sentences in half. Combine short ones. Move the most important point to the very first or very last sentence.
5.  **Verify constraints:** Ensure no emojis, no em dashes, and no "Furthermore/Moreover" style transitions.

## Examples

### Example 1: Project README
**Input:** Write a simple README for a project called "my-tools." Mention it's based on things found on Reddit.
**Output:**
# my tools

these are some scripts i put together for my own use. i based them on different things i found on reddit from people sharing their setups.

mostly just simple stuff to help with different tasks. i keep them here to stay organized and make it easier to load them when i need them.

### Example 2: Team Email
**Input:** Tell the team the release is delayed by 2 days because of a bug in the auth flow.
**Output:**
Hey everyone,

We have to push the release back two days. There's a bug in the login flow that we need to fix first. 

I'm sorry for the late notice, but I'd rather ship it right than ship it broken. Let me know if you have questions.
