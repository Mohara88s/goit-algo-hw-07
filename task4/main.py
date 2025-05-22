class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.is_deleted = False
        self.replies = []

    def add_reply(self, reply_comment:"Comment"):
        self.replies.append(reply_comment)

    def display(self, level=0):
        print(f'{'    ' * level}{self.author and f'{self.author}: '}{self.text}')
        for reply in self.replies:
            reply.display(level + 1)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
        self.author = ''


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()