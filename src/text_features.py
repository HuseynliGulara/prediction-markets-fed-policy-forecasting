def hawkishness_score(text, hawkish_words, dovish_words):
    words = text.lower().split()

    hawkish = sum(
        word.strip(".,;:()[]\"'") in hawkish_words
        for word in words
    )

    dovish = sum(
        word.strip(".,;:()[]\"'") in dovish_words
        for word in words
    )

    total_words = len(words)

    if total_words == 0:
        return 0

    return (hawkish - dovish) / total_words * 1000