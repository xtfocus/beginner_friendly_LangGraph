In this branch, we see how LangGraph implements history (aka memory).

Since LangGraph is basically an extension of LangChain, it's kinda beneficial to know how LangChain implements history.

- https://python.langchain.com/v0.1/docs/modules/memory/
- https://python.langchain.com/v0.2/docs/integrations/memory/
- https://www.reddit.com/r/LangChain/comments/1dabjys/comment/l7jmaf7/
- https://github.com/langchain-ai/langgraph/blob/7a164dab0944c70311962407d3ff3b995c526054/examples/managing-conversation-history.ipynb

(The docs on memory was more detailed in v0.1)

TLDR; chatbot need memory to be prompted to keep conversation developing; memory too big is an issue, some manipulation is helpful here.

# Why memory

When you use ChatGPT WebUI, the chatbot can remember your questions from the same session. This is possible because each time you ask it a new question, the backend save the interaction (as an array or any other data structure), this save is memory.\
Next time, when you ask another question, not only the new question is prompted, but the whole memory (or a modified version of it). This way, the chatbot keeps track of all the references you made, making the conversation more human-like.

Without memory, ChatGPT would be just GPT - a very clever goldfish, but still just a goldfish.

# Modified memory

In the purest form, memory is a record of interactions between you and the LLM application (ChatGPT for instance):
- What YOU have said
- What's the bot final response
- And anything in between: immediate outputs of the LLM application (tool calling details, error messages, reasoning steps, etc)
- Heck yeah, you can add timestamps to memory, if you have to

As the conversation grows, so does the size of this memory. This:
- stresses the context limit of LLMs, likely deteriorating conversation quality over time.
- slower response over time
- costs (incrementally) more tokens over time (\$\$\$)

This leads to the need to optimize memory:
- make it smaller
- make it more concise

Be open-minded: It's entirely possible that being concise requires making the history longer.
