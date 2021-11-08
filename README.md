# Django REST Client API
Client data provider API.

You can check this application working at: https://drf-clients-api.herokuapp.com/

Documentation: https://drf-clients-api.herokuapp.com/doc


## Features

#### Endpoints

GET /clients -> Display all the clients data stored in the database.


POST /clients -> Create a new client.


GET /clients/cpf_filter/{cpf} -> Display the client with the specified cpf. -
example: /clients/cpf_filter/94099913236


GET /clients/gender_filter/{gender} -> Display all the clients with the specified gender. -
example: /clients/gender_filter/F

GET /clients/state_filter/{state} -> Display all the clients that live in the specified state. -
example: /clients/state_filter/Acre


GET /clients/{id}/ -> Display the client with the specified id. - 
example: /clients/350


#### Searching and ordering

It is possible to search for a clients name by using the search tool located
on the top right corner. On the same menu it is also possible to order the clients 
data by their date of birth.

#### Pagination

This API has the pagination resource implemented, which means that dont matter how many
clientes are registered, only 100 will be displayed per page.

#### Query Parameter Versioning

This api has 2 versions. When adding the query parameter "?version=v2" to the URL,
two more fields will be displayed for each client: RG and cellphone number.

#### Validation

When creating a new client using  POST, each field has its own validation criteria, 
which is necessary to be respected in order for the creation to work.




