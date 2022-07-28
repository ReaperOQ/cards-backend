class Card:
    def __init__(self, id: int, collection_id: int, picture: str, title: str, type: str, rarity: str,
                 skills: dict[int | str | float]):
        self.id = id
        self.collection_id = collection_id
        self.picture = picture
        self.title = title
        self.type = type
        self.rarity = rarity
        self.skills = skills

    def dict(self):
        return {
            'id': self.id,
            'collection_id': self.collection_id,
            'picture': self.picture,
            'title': self.title,
            'type': self.type,
            'rarity': self.rarity,
            'skills': self.skills
        }

    def printable(self):
        skills = '\n\t\t'.join(f'{skill} -- {self.skills[skill]}' for skill in self.skills.keys())
        return f'Id: {self.id}\n' \
               f'Collection: {self.collection_id}\n' \
               f'Picture URL: {self.picture}\n' \
               f'Title: {self.title}\n' \
               f'Type: {self.type}\n' \
               f'Rarity: {self.rarity}\n' \
               f'Skills: {skills}'


class CardCollection:
    def __init__(self, id: int, title: str, cards: list[Card] = None):
        if cards is None:
            cards = []
        self.id = id
        self.title = title
        self.cards = cards

    def add(self, card: Card):
        self.cards.append(card)

    def remove(self, card_id: int):
        for c in self.cards:
            if c.id == card_id:
                self.cards.remove(c)

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'cards': [card.dict() for card in self.cards]
        }

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        return len(self.cards)


collection1 = CardCollection(1, 'SampleCol')
# collection1.add(Card(1, 1, 'some_url', 'SampleCard', 'SampleType', 'Rare', {'Power': 5, 'Agility': 3}))
# print(collection1[1].printable())
# print(len(collection1))
