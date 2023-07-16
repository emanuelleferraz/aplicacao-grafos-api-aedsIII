import requests
import json
import amount_votes

class Graph:

  # Estrutura de dados Grafo
  def __init__(self) -> None:
    self.adj_list = {}
    self.node_count = 0
    self.edge_count = 0

  def add_node(self, node):
    if node in self.adj_list:
      return
    self.adj_list[node] = {}
    self.node_count += 1

  def add_edge(self, node1, node2):
    if node1 not in self.adj_list:
      self.add_node(node1)

    if node2 not in self.adj_list:
      self.add_node(node2)

    if node2 in self.adj_list[node1]:
      self.adj_list[node1][node2] += 1
      return
      
    else:  
      self.adj_list[node1][node2] = 1
      self.edge_count += 1

  # Construção do Grafo de Deputados usando consumo de API
  def deputies_graph(self):
    favor = []
    against = []
    a = amount_votes.AmountVotes()
    voting_ids = requests.get(
      "https://dadosabertos.camara.leg.br/api/v2/votacoes?dataInicio=2022-01-01&ordem=DESC&ordenarPor=dataHoraRegistro"
    )

    voting_ids = voting_ids.json()

    control_1 = 0
    while control_1 < len(voting_ids["dados"]):
      votings = voting_ids["dados"][control_1]
      voting = "https://dadosabertos.camara.leg.br/api/v2/votacoes/" + votings[
        "id"] + "/votos"
      votes = requests.get(voting)
      votes = votes.json()

      control_2 = 0
      while control_2 < len(votes["dados"]):
        if votes["dados"] != []:
          analyze_vote = votes["dados"][control_2]
          if analyze_vote["tipoVoto"] == "Sim":
            favor.append(analyze_vote["deputado_"]["nome"])
          elif analyze_vote["tipoVoto"] == "Não":
            against.append(analyze_vote["deputado_"]["nome"])
          if analyze_vote["deputado_"]["nome"] not in a.adj_list:
            a.adj_list[analyze_vote["deputado_"]["nome"]] = 1
          else:
            a.adj_list[analyze_vote["deputado_"]["nome"]] += 1
        control_2 += 1

      control_3 = 0
      while control_3 < len(favor):
        deputy = favor[control_3]
        control_4 = 0
        while control_4 < len(favor):
          deputy2 = favor[control_4]
          if deputy == deputy2:
            control_4 += 1
            continue
          self.add_edge(deputy, deputy2)
          control_4 += 1
        control_3 += 1

      control_5 = 0
      while control_5 < len(against):
        deputy = against[control_5]
        control_6 = 0
        while control_6 < len(against):
          deputy2 = against[control_6]
          if deputy == deputy2:
            control_6 += 1
            continue
          self.add_edge(deputy, deputy2)
          control_6 += 1
        control_5 += 1

      favor = []
      against = []
      control_1 += 1

    a.arquive()

  # Armazenando os dados no arquivo
  def write_arq(self):
    dep_list = []
    with open("votacaoVotos-2022-graph.txt", 'w') as file:
      file.write(f"{self.node_count} {self.edge_count}\n")
      for deputy in self.adj_list:
        for deputy2 in self.adj_list[deputy]:
          if deputy not in dep_list:
            file.write(f"{deputy} {deputy2} {self.adj_list[deputy][deputy2]}\n")
        dep_list.append(deputy)
