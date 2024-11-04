#Ler um vetor com 20 idades e exibir a maior e menor.

idades = []
for i in range(1,21):
    idade = int(input(f"digite a idade {i}:   "))
    idades.append(idade)

print("a maior idade das idades digitadas é:", max(idades))
print("a menor idade das idades digitadas é:", min(idades))
