###################### load packages ####################
import config

###################### main函数 ####################
def main():

    ########### 读取配置文件 ##########
    ch = config.ConfigHandler("./config.ini")
    ch.load_config()

    ########### 读取参数 ##########
    max_query_len_char = int(ch.config["data"]["max_query_len_char"])
    max_query_len_word = int(ch.config["data"]["max_query_len_word"])
    char_voc_size = int(ch.config["data"]["char_voc_size"])
    word_voc_size = int(ch.config["data"]["word_voc_size"])
    char_embedding_size = int(ch.config["model"]["char_embedding_size"])
    word_embedding_size = int(ch.config["model"]["word_embedding_size"])
    dropout_keep_prob = float(ch.config["model"]["dropout_keep_prob"])
    batch_size = int(ch.config["model"]["batch_size"])
    num_epochs = int(ch.config["model"]["num_epochs"])
    learning_rate = float(ch.config["model"]["learning_rate"])
    class_size = int(ch.config["model"]["class_size"])

    ########### 查看参数 ##########
    print("max_query_len_char:")
    print(max_query_len_char)

    print("max_query_len_word:")
    print(max_query_len_word)

    print("char_voc_size:")
    print(char_voc_size)

    print("word_voc_size:")
    print(word_voc_size)

    print("char_embedding_size:")
    print(char_embedding_size)

    print("word_embedding_size:")
    print(word_embedding_size)

    print("dropout_keep_prob:")
    print(dropout_keep_prob)

    print("batch_size:")
    print(batch_size)

    print("num_epochs:")
    print(num_epochs)

    print("learning_rate:")
    print(learning_rate)

    print("class_size:")
    print(class_size)


if __name__ == "__main__":
    main()
