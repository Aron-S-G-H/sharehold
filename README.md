## 🛠 Installation
1. **Clone the repository**
   
   `git clone https://github.com/Aron-S-G-H/sharehold.git`
   
   `cd sharehold`
2. **Add script.sql file**
   <p>Make sure the file name is exactly script.sql.</p>

3. **Run docker-compose**
   <p>Make sure you have installed docker and docker compose plugin on your system</p>
   
   `docker compose up -d --build`
4. **Setup DB**
   <p>create bahoosh database</p>
  
   `docker exec -t sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P Root1234!e -Q 'CREATE DATABASE bahoosh;'`

   <p>run script.sql</p>

   `docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P Root1234!e -d bahoosh < ./docker-entrypoint-initdb.d/init.sql`

5. **Setup ElasticSearch**
   
   ` docker exec -it shareHold bash `
   
   `python manage.py search_index --rebuild`
   
   now visit localhost:80 and everything should be fine
