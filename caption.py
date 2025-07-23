import random


def generate_caption(keywords):
    captions = [
        f"Embracing {keywords}! 💖 #Inspiration #LoveLife",
        f"The magic of {keywords} awaits! ✨ #DreamBig #Achieve",
        f"Forever inspired by {keywords}. 💪 #Motivation #StayPositive",
        f"Discover the beauty of {keywords}. 🌸 #Nature #Adventure",
        f"Let's celebrate {keywords} together! 🥳 #Joy #Togetherness",
    ]

    hashtags = [
        "#SocialMedia", "#InstaGood", "#CaptionThis", "#NewPost",
        "#Trending", "#StoryTelling"
    ]

    selected_caption = random.choice(captions)
    selected_hashtags = random.sample(hashtags, 3)

    return f"{selected_caption}\n{' '.join(selected_hashtags)}"


if __name__ == "__main__":
    user_input = input("Enter keywords or themes for your post: ")
    print("Generated Caption:\n")
    print(generate_caption(user_input))

