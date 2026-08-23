#include <stdio.h>
#include <locale.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

    struct ficha_funcionario{
        char nome[100];
        char cpf[16];
        float credito;
        char endereco[100];
        char cep[16];
        char cidade[20];
        char estado[3];
    };

void limpar() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void remover_quebra_linha(char *str) {
    size_t len = strlen(str);
    if (len > 0 && str[len-1] == '\n') {
        str[len-1] = '\0';
    }
}

void cadastrar(){
    limpar();
    setlocale(LC_ALL, "Portuguese");
    
    FILE *arquivo = fopen("funcionarios.txt", "a+");

    struct ficha_funcionario funcionario;
    
    char retornar[]= "";

    char buffer[500];

    char credito_temporario[500] = "";

    char cep_temporario[10] = "";

    printf("Sistema de cadastro\n");
    printf("Preencha o campo de informações: \n");

    printf("Digite o seu nome: \n");
    scanf(" %[^\n]", funcionario.nome);

    printf("Digite o seu CPF (cujo esse será seu identificador): \n");
    scanf("%s", funcionario.cpf);

    printf("Digite o seu limite de crédito: \n");
    scanf(" %[^\n]", credito_temporario);
    funcionario.credito = atof(credito_temporario);

    printf("Digite o seu endereço: \n");
    scanf(" %[^\n]", funcionario.endereco);

    printf("Digite o seu cep: \n");
    scanf(" %s", funcionario.cep);

    printf("Digite a sua cidade: \n");
    scanf(" %19[^\n]", funcionario.cidade);

    printf("Digite o estado em que mora: \n");
    scanf("%s", funcionario.estado);

    funcionario.credito = atof(credito_temporario);

    fprintf(arquivo, "%s,", funcionario.nome);
    fprintf(arquivo, "%s,", funcionario.cpf);
    fprintf(arquivo, "%f,", funcionario.credito);
    fprintf(arquivo, "%s,", funcionario.endereco);
    fprintf(arquivo, "%s,", funcionario.cep);
    fprintf(arquivo, "%s,", funcionario.cidade);
    fprintf(arquivo, "%s", funcionario.estado);
    fprintf(arquivo, "%s", "\n");

    fclose(arquivo);

    printf("Cadastro concluído!\n");
    printf("Digite qualquer valor para retornar: ");
    scanf("%s", retornar);
    limpar();
}

void excluir_cadastro(){
    limpar();
    char retornar[] = "";
    FILE *arquivo, *temporario;
    arquivo = fopen("funcionarios.txt", "r+");
    temporario = fopen("temp.txt", "w+");

    char cpf_buscar[16] = "";

    printf("Digite o seu CPF: \n");
    scanf("%s", cpf_buscar);


    struct ficha_funcionario listar;

    char linha[500];
    int encontrou = 0;

    while (fgets(linha, sizeof(linha), arquivo) != NULL) {
        char cpf_atual[16];
        char nome[100];
        
        sscanf(linha, "%99[^,],%15[^,],", nome, cpf_atual);
        
        if (strcmp(cpf_buscar, cpf_atual) != 0) {
            fprintf(temporario, "%s", linha);
        } else {
            encontrou = 1;
        }
    }

    fclose(temporario);
    fclose(arquivo);

    remove("funcionarios.txt");
    rename("temp.txt", "funcionarios.txt");

    printf("Cadastro excluido!\n");
    printf("Digite qualquer valor para retornar: ");
    scanf("%s", retornar);
    limpar();

}

void alterar_cadastro(){
limpar();
char retornar[] = "";
FILE *arquivo, *temporario;
arquivo = fopen("funcionarios.txt", "r");
temporario = fopen("temp.txt", "w");

char cpf_buscar[16] = "";

printf("Digite o CPF do cadastro que deseja alterar: \n");
scanf("%15s", cpf_buscar);

char linha[500];
int encontrou = 0;

while (fgets(linha, sizeof(linha), arquivo) != NULL) {
char cpf_atual[16];
char nome[100];

sscanf(linha, "%99[^,],%15[^,],", nome, cpf_atual);

if (strcmp(cpf_buscar, cpf_atual) != 0) {
fprintf(temporario, "%s", linha);
} else {
encontrou = 1;

struct ficha_funcionario funcionario;
char credito_temporario[500] = "";

strcpy(funcionario.cpf, cpf_atual);

printf("Cadastro encontrado! Digite os novos dados: \n");

printf("Digite o novo nome: \n");
scanf(" %99[^\n]", funcionario.nome);

printf("Digite o novo limite de crédito: \n");
scanf(" %[^\n]", credito_temporario);
funcionario.credito = atof(credito_temporario);

printf("Digite o novo endereço: \n");
scanf(" %99[^\n]", funcionario.endereco);

printf("Digite o novo cep: \n");
scanf(" %15s", funcionario.cep);

printf("Digite a nova cidade: \n");
scanf(" %19[^\n]", funcionario.cidade);

printf("Digite o novo estado: \n");
scanf("%2s", funcionario.estado);

fprintf(temporario, "%s,", funcionario.nome);
fprintf(temporario, "%s,", funcionario.cpf);
fprintf(temporario, "%f,", funcionario.credito);
fprintf(temporario, "%s,", funcionario.endereco);
fprintf(temporario, "%s,", funcionario.cep);
fprintf(temporario, "%s,", funcionario.cidade);
fprintf(temporario, "%s", funcionario.estado);
fprintf(temporario, "%s", "\n");
        }
    }

fclose(temporario);
fclose(arquivo);

remove("funcionarios.txt");
rename("temp.txt", "funcionarios.txt");

if (!encontrou) {
printf("CPF não encontrado!\n");
} else {
printf("Cadastro alterado com sucesso!\n");
    }

printf("Digite qualquer valor para retornar: ");
scanf("%s", retornar);
limpar();
}


int main(){
    setlocale(LC_ALL, "Portuguese");
    srand(time(NULL));
    int escolha = 0;

    while (true){
        printf("Bem-vindo ao sistema de funcionários da Hells Market!\n");
        printf("Escolha uma das opções:\n1 - Cadastrar Funcionário \n2 - Excluir Cadastro\n3 - Alterar Cadastro\n->");
        scanf("%d", &escolha);

        while (getchar() != '\n');


        if (escolha == 1){
            cadastrar();
        }

        else if (escolha == 2){
            excluir_cadastro();
        }

        else if (escolha == 3){
            alterar_cadastro();
        }

    }
}