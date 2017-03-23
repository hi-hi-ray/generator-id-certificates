# generator-id-certificates
Generator of Numbers for Certificates

## How To Use. :clipboard:

- First of all, copy the file: **informations.json.example** and paste at the same folder, don't forget to rename it to **informations.json**  and fill all the informations.
- Second and Last Step, Run the file application.py.

Running the application:
```python
    python ".\application\application.py"
```

## What should do. :confetti_ball:

This application will read your informations and create a text file with ids for you put on your certificates. You can display these ids wherever you want to prove that you generate that certificate.

## Filling the Json. :pencil:

- organization_name: Here you must insert the name of your organization.
- organization_abbreviation: Here you must insert an abbreviation of your organization.
- event_name: Here you must insert the name of your event.
- quantity_of_characters: Here you must insert the length of the id that you desire. The id will be composed by the abbreviation-Random letters and numbers.
- quantity_of_certificates: Here you must insert the quantity of certificates you want.
- path_to_save_file: Here you must insert the path to where you want to be save the file with the generated ids. For your convenience we generate a file with all the ids.

Don't forget to look the **Types** to check what we are expecting.

## Types. :books:

- organization_name: String.
- organization_abbreviation: String.
- event_name: String.
- quantity_of_characters: Integer.
- quantity_of_certificates: Integer.
- path_to_save_file: String.

--------------
# generator-id-certificates
Gerador de Números para Certificados

## Como Usar. :clipboard:

- Primeiro, copie o arquivo: **informations.json.example** e cole na mesma pasta, não se esqueça de renomeá-lo para **informations.json** e preencha todas as informações.
- Segundo e Passo final, Rode o arquivo application.py.

Rodando a applicação:
```python
    python ".\application\application.py"
```

## O que deve fazer. :confetti_ball:

Esta aplicação irá ler as suas informações e criar um arquivo de texto com os ids para você colocar no seu certificado. Você pode exibir a lista destes ids onde você desejar provar que você gerou esse certificado.

## Preenchendo Json. :pencil:

- organization_name: Aqui você deve inserir o nome de sua organização.
- organization_abbreviation: Aqui você deve inserir uma abreviação de sua organização.
- event_name: Aqui você deve inserir o nome do seu evento.
- quantity_of_characters: Aqui você deve inserir o comprimento do id que você deseja. O id será composto pela abbreviation-letras e números aleatórios.
- quantity_of_certificates: Aqui você deve inserir a quantidade de certificados que deseja.
- path_to_save_file: Aqui você deve inserir o caminho para onde você quer salvar o arquivo com os ids gerados. Para sua conveniência geramos um arquivo com todos os ids.
Não se esqueça de olhar o **Tipos** para verificar o que estamos esperando.

## Tipos. :books:

- organization_name: String.
- organization_abbreviation: String.
- event_name: String.
- quantity_of_characters: Integer.
- quantity_of_certificates: Integer.
- path_to_save_file: String.
