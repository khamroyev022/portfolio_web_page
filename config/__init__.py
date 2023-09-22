class Talaba:
    def __init__(self, ism, familiya, sharif, tugilgan_yili, fakultet, guruh):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.tugilgan_yili = tugilgan_yili
        self.fakultet = fakultet
        self.guruh = guruh
        self.kurs = 2004

    def kurs_update(self):
        self.kurs += 1 
        return self.kurs

a = Talaba('Anvar', 'Sanoyev', 'Komilovo', 2003, 'Axborot Texnologiyalari', 'ATT')

a.kurs_update()
a.kurs_update()

print(a.kurs)
