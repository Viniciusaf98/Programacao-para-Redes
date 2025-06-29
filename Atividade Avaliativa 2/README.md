[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bLFSiwcw)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17581726&assignment_repo_type=AssignmentRepo)
<h1>Atividade Avaliativa #02 - SOCKETS - PortScan</h1>

> [!WARNING]
> 1. Os programas deverão ser desenvolvidos em linguagem PYTHON;
> 2. Cada questão deverá ser respondida em arquivos em separado;
> 3. As respostas deverão ser submetidas no link correspondente a essa lista disponível no Moodle;
> 4. Atentem para o prazo de submissão. Não serão aceitos envios posteriores a data limite.  

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>Questão 01:</summary>
  <br/>
  Na URL https://pt.wikipedia.org/wiki/Lista_de_portas_dos_protocolos_TCP_e_UDP são listadas as portas UDP e TCP relativas a cada serviço.<br/><br/>

  Com base na listagem das portas 0 a 995 (gerem um arquivo de input contendo a listagem das portas, o seu respectivo protocolo e sua descrição), desenvolva um programa para verificar em um determinado
HOST (a ser solicitado pelo programa) quais portas respondem ou não a conexão a ser estabelecida de acordo com o seu respectivo protocolo (TCP ou UDP). Note que determinadas portas tanto aceitam
conexão UDP quanto TCP.<br/><br/>

  Vocês tanto poderão utilizar o método <b>connect()</b> quanto o método <b>connect_ex()</b> da classe Socket.<br/><br/>

  O output será em um arquivo no formato JSON (<b>teste_porta.json</b>) a ser obrigatoriamente salvo na mesma pasta/diretório do programa e deverá estar no seguinte formato:<br/>

  ```
  [
    { 1: { 'porta': NNNNN, 'protocolo': 'PPPPP – DDDDD', 'status': 'SSSSS'} ,
    { 2: { 'porta': NNNNN, 'protocolo': 'PPPPP – DDDDD', 'status': 'SSSSS'} ,
    ...,
    { n: { 'porta': NNNNN, 'protocolo': 'PPPPP – DDDDD', 'status': 'SSSSS'} ,
  ]
  ```

  Onde:<br/>

  * <b>NNNNN</b> será o número da porta que está sendo testada;<br/>
  * <b>'PPPPP – DDDDD'</b> será uma string com o protocolo (<b>PPPPP</b>) e a descrição (<b>DDDDD</b>);<br/>
  * <b>'SSSSS'</b> será uma string com o status do teste, que pode ser OK ou o erro que deu.<br/>
  <br/><br/>
</details>


