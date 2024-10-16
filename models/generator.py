from transformers import pipeline

def generate_content_ideas(news_data):
    generator = pipeline('text-generation', model='gpt2')
    ideas = []
    for news in news_data:
        prompt = f"Suggest a creative content idea based on: {news}"
        idea = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        ideas.append(idea)
    return ideas
