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

  # Construção do Grafo de Deputados usando API
  def deputies_graph(self):
    favor = []
    against = []
    a = amount_votes.AmountVotes()
    voting_ids = requests.get(
      "https://dadosabertos.camara.leg.br/api/v2/votacoes?dataInicio=2022-01-01&ordem=DESC&ordenarPor=dataHoraRegistro"
    )

    voting_ids = voting_ids.json()

    for i in range(len(voting_ids["dados"])):
      votings = voting_ids["dados"][i]
      voting = "https://dadosabertos.camara.leg.br/api/v2/votacoes/" + votings[
        "id"] + "/votos"
      votes = requests.get(voting)
      votes = votes.json()
      for i in range(len(votes["dados"])):
        if votes["dados"] != []:
          analyze_vote = votes["dados"][i]
          if analyze_vote["tipoVoto"] == "Sim":
            favor.append(analyze_vote["deputado_"]["nome"])
          elif analyze_vote["tipoVoto"] == "Não":
            against.append(analyze_vote["deputado_"]["nome"])
          if analyze_vote["deputado_"]["nome"] not in a.adj_list:
            a.adj_list[analyze_vote["deputado_"]["nome"]] = 1
          else:
            a.adj_list[analyze_vote["deputado_"]["nome"]] += 1

      for deputy in favor:
        for deputy2 in favor:
          if deputy == deputy2:
            continue
          self.add_edge(deputy, deputy2)

      for deputy in against:
        for deputy2 in against:
          if deputy == deputy2:
            continue
          self.add_edge(deputy, deputy2)

      favor = []
      against = []

    a.arquive()

  # Armazenando os dados no arquivo
  def write_arq(self):
    dep_descobertos = []
    with open("votacaoVotos-2022-graph.txt", 'w') as file:
      file.write(f"{self.node_count} {self.edge_count}\n")
      for dep in self.adj_list:
        for dep2 in self.adj_list[dep]:
          if dep2 not in dep_descobertos:
            file.write(f"{dep} {dep2} {self.adj_list[dep][dep2]}\n")
        dep_descobertos.append(dep)
