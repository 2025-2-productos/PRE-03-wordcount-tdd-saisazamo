import os


def write_word_counts(output_folder, word_counts):

    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "wordcount.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f"{word}\t{count}\n")
