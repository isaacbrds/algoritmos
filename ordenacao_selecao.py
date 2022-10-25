def busca_menor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice


def ordenacao_por_selecao(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = busca_menor(arr)
    novoArr.append(arr.pop(menor))
  return novoArr


print(ordenacao_por_selecao([1,3,5,0,20,4]))