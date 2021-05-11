# Minikube

Setting up minikube

1. In /etc/hosts set a sample domain name using the minikube ip. You can get it by using the below command

   ```
   echo $(minikube ip)
   ```

2. In /etc/hosts, we will then be setting up the domains for our Keycloak, Oauth and Application

   ```
   <paste you minikube ip here> domain_name.com
   <paste you minikube ip here> keycloak.domain_name.com
   <paste you minikube ip here> auth.domain_name.com
   ```

   For this demo we will be using `domain_name` as `ratanboddu`

3. Ensure that you have the `nginx-ingress` addon enabled. You can use below command to verify

   ```
   minikube addons list
   ```

   If you dont have it enabled, you can use the below command to enable it.

   ```
   minikube addons enable ingress
   ```

# Keycloak

User authentication and authorization tool

- Deploying Keycloak
- Configuring Keycloak

## Deploying Keycloak

1.  Navigate to the `keycloak` folder and set the necessary environment variables for Keycloak. [More information on variable here](https://hub.docker.com/r/jboss/keycloak/)

    a. KEYCLOAK_USER : default User

    b. KEYCLOAK_PASSWORD : default password

    c. PROXY_ADDRESS_FORWARDING: enabling proxy address forwarding

    d. DB_VENDOR : specifying the db vendor. Can be one of the following:

         - `h2` for the embedded H2 database

         - `postgres` for the Postgres database

         - `mysql ` for the MySql database

         - `mariadb` for the MariaDB database

         - `oracle` for the Oracle database

         - `mssql` for the Microsoft SQL Server database

    e. DB_ADDR : hostname of the DB being used

    f. DB_PORT : port of the database (optional, default is DB vendor default port)

    g. DB_DATABASE : name of the database to use (optional, default is keycloak)

    h. DB_USER : user to use to authenticate to the database (optional, default is '')

    i. DB_PASSWORD : user's password to use to authenticate to the database (optional, default is '')

2.  After successfully updating all the necessary values, we can deploy all the yamls using the below command

    ```
    kubectl apply -f keycloak/.
    ```

### Configuring Keycloak

1. In the Left-Side menu item "Client Scopes", click "Create"

2. Create a new client scope called `api` with the default settings

3. Click on the `Mappers` tab, create a new mapper called `groups` with below settings and Save.
   [CreateProtocolMapper](/images/CreateProtocolMapper.png)

4. Click `Add Builtin` and add `username`, `email`, `profile`.
   [AddBuiltin](/images/AddBuiltin.png)

5. Add this newly created scope to your existing Client at
   `Clients -> Your_Client_Name -> Client Scopes`
   Select the newly created sccope `api` at the left box and click `Add selected` for `Default Client Scopes`
   NOTE: You client should have `Valid Redirect URI` set to `http://<your_domain_name>/oauth2/callback`

#### We have now completed deploying and configuring Keycloak, which will now send the correct tokens to OAuth2-proxy.

# OAuth2 Proxy

### Deploying OAuth2 Proxy

1.  Navigate to the `oauth2-proxy` folder and set the necessary vallues in the `oauth_configmap.yaml`

    - For the `login_url`, `redeem_url`, `validate_url`, replace the domain name to your `domain_name`

    - Set the `client_id` by navigating to

      `Clients (Left Navbar)-> Your Client -> Client ID`

    - Set the `client_secret` by navigating to

      `Clients (Left Navbar)-> Your Client -> Credentials Tab -> Secret`

    - Set the `cookie_secret` : To generate a strong cookie secret use `python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(16)).decode())'`

    - Set the `cookie_refresh` : To refresh the cookie after this duration

    - Set the `keycloak_group` if you want to authenticate on the basis of groups. Only users having this group will be able to access the application

    - For `cookie_domains` and `whitelist_domains`, replace the domain name with your `domain_name`

      For more details on the remaining values you can refer [here](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/)

2.  Navigate to the `oauth2-proxy` folder and set the necessary vallues in the `oauth_configmap2.yaml`

    - Here, we need tp update the Keycloak URL for Logout in the `error.html` section

3.  After successfully updating all the necessary values, we can deploy all the yamls using the below command

```
kubectl apply -f oauth2-proxy/.
```
