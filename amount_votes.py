class AmountVotes:

  def __init__(self):
    self.adj_list = {}

  # Cria o arquivo que armazena a quantidade de votos de cada deputado  
  def arquive(self):
    with open("amount-votes-deputies.txt", 'w') as file:
      for deputy in self.adj_list:
        file.write(f"{deputy} {self.adj_list[deputy]}\n")