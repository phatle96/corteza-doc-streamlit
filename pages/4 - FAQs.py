import streamlit as st

st.set_page_config(page_title="Frequently Asked Questions", layout="wide")

st.markdown("# Frequently Asked Questions")
st.sidebar.markdown("# Frequently Asked Questions")

st.expander("1 - How to set up a Corteza instance?", expanded=False).markdown("""
To create a Corteza instance, you will need to set up a database and configure the Corteza server. Here are the steps, based on information in the sources:

**1. Database Setup:**

- Corteza supports **PostgreSQL and MySQL** as database engines. It is strongly recommended to use these instead of SQLite for production environments, as SQLite can lead to data loss.
- If you choose to use **SQLite**, ensure that you are using persistent storage, as the database is re-created whenever a new connection is established, and dropped when the last connection is closed.
- To set up a **MySQL** database using Docker, you can use the provided commands which create a database named `corteza` and a user with the required privileges:
    
    ```
    docker run --name $DOCKER_NAME -e MYSQL_ROOT_PASSWORD=$ROOT_PWD -d -p $MYSQL_PORT:3306 percona:8.0;
    docker exec -it $DOCKER_NAME mysql -uroot -p$ROOT_PWD;
    CREATE DATABASE corteza;
    CREATE USER 'corteza'@'172.17.0.1' IDENTIFIED BY 'corteza';
    GRANT ALL PRIVILEGES ON corteza.* TO 'corteza'@'172.17.0.1';
    FLUSH PRIVILEGES;
    ```
    
- A template is provided to construct the `DB_DSN` variable, which is used to connect to the database.

**2. Corteza Server Installation:**

- Corteza can be deployed on any system that can run **Docker**. If you wish to deploy Corteza elsewhere, you will need to compile your own binaries.
- The **DevOps Guide** walks you through the installation process for both demo/development and production-like environments.
- You can download prebuilt sources from the releases page or build your own.
- The DevOps guide also provides information about system and Corredor configurations, offline/online deployment examples, data backups, and troubleshooting.
- The guide also provides instructions on how to set up a supported database engine and change the `DB_DSN` variable in the `.env` file.
- The `HTTP_ADDR` .env variable needs to be set to match your local environment; for example, `HTTP_ADDR=localhost:80`.

**3. Docker Compose:**

- **Docker Compose** can be used to run multiple Docker images, where each can be arbitrarily configured.
- When using `.env` files with Docker Compose, you need to explicitly specify this inside the `docker-compose.yaml` file. For example:
    
    ```
    version: '3.5'
    services:
      server:
        image: cortezaproject/corteza:${VERSION}
        restart: always
        env_file: [ .env ] # <- see here
        depends_on: [ db ]
        ports: [ "127.0.0.1:18084:80" ]
    ```
    
- It is important that containers are on the same network.

**4. Running the Services:**

- Run `docker-compose up -d` to start all of the services configured in your `docker-compose.yaml` file.
- The execution of this command can take a few seconds.
- You can follow the `docker-compose` logs.
- You can use the `docker-compose ps` command to check the health from the CLI.

**5. Initial Configuration:**

- After starting the server, you may need to perform a **provision** step to ensure that initial resources (users, roles, namespaces) are imported from the provision files.
- Corteza provides a command-line interface (CLI) that can be used for various tasks, including importing data, managing users, and upgrading the system.

**6. Accessing Corteza:**

- Once the server is running, you can access the web applications through a browser.
- The server can serve all of the web applications for cases where you need to quickly test something on a user interface.

**Important Considerations:**

- When using modified versions of `corteza-js` and `corteza-vue`, make sure to link them using `yarn link`.
- The `HTTP_SSL_TERMINATED` setting is used to indicate that SSL termination is enabled in a proxy or load balancer in front of Corteza.
- Make sure to adjust the location of assets if you've defined a custom configuration that affects the base path.
- Corteza provides a web console to access important server information.
- The `AUTH_PROVISION_SUPER_USER` variable can be set to create one or more users with the configured values using the provided email as a password, but should not be used in production.
- Corteza uses the OAuth2 flow for user authentication.
- When using the same server for both authentication and processing, you can skip setting the `CortezaAuth` API.

By following these steps and referring to the relevant sections of the documentation, you should be able to create a functional Corteza instance.
""")


st.expander("2 - How to add a database connection to Corteza?", expanded=False).markdown("""
To add a database connection to Corteza, you will need to configure a new connection through the Admin panel, specifying the connection type and parameters. Here's how, based on the sources:

**1. Access the Connection Management Interface:**

- Navigate to the **{PRODUCT_NAME} {APP_NAME_ADMIN}** panel.
- Go to the **menu:system[connections]** section.

**2. Create a New Connection:**

- Click on the **btn:[add connection]** button.
- Fill out the form with the necessary details.

**3. Specify Connection Parameters:**

- The **connection parameters** depend on the selected connection type.
- You need to specify the connection type and the connection parameters based on the database you want to connect to.
- The sources mention that only connections to the following RDBMS databases are supported:
    - **MySQL**
    - **PostgreSQL**
    - **SQLite**

**4. Connection Types:**

- **corteza::dal:connection:dsn:** This connection type uses a **DSN (Data Source Name) string** to connect to the database.
    - The configuration parameters must be provided in the following JSON format: `{"dsn": ""}`.
    - The specific syntax for the DSN depends on the database you are using. Examples of DSN strings are provided for MySQL and PostgreSQL.
- The sources don't specify other connection types for databases.

**5. Connection Identifier:**

- The **collection or database table name** specifies where the module's records are stored inside the connection.
- If the identifier is omitted, the connection-defined identifier is used; if the connection doesn't provide a default, the system default is used.
- For some scenarios, {PRODUCT_NAME} can create the appropriate structures if they don't already exist in the connection, such as a new table in an RDBMS database.

**6. Important Considerations:**

- The list of connections includes only **external connections**; the primary connection is available at the top of the list.
- You can define as many connections as you need.
- You can connect to databases with already existing data, removing the need to migrate it over to {PRODUCT_NAME}.
- Changing the connection will **reset the sensitivity level configuration** on the module and fields if the sensitivity level is incompatible with the new connection.
- If the connection is misconfigured or unable to connect, a list of identified issues will be presented in the connection configuration screen.

By following these steps, you can successfully add a database connection to your Corteza instance.                                                 
""")

st.expander("3 - How to integrate Corteza with other applications?", expanded=False).markdown("""
To integrate Corteza with other applications, you can use its **API**, **authentication** capabilities, and **integration gateway**. Here's how, based on the provided sources:

**1. Using the REST API:**

- Corteza is **API-centric**, meaning that almost everything can be done via an API endpoint.
- You can access Corteza's data and functionality using its **REST API**.
- The API uses **JSON** for data exchange.
- Corteza provides **JavaScript API clients (SDKs)** that can be used to interact with the API.
    - These API clients are available in the `@cortezaproject/corteza-js` package.
    - The package includes clients for `System`, `Compose`, `Automation`, and `Federation`.
    - You can import the API clients using `import { apiClients } from '@cortezaproject/corteza-js'`.
- You can find the API documentation for Corteza server at [https://docs.cortezaproject.org/corteza-api-docs/corteza-server/{PAGE-VERSION}/index.html](https://docs.cortezaproject.org/corteza-api-docs/corteza-server/%7BPAGE-VERSION%7D/index.html).
- The API documentation for Corteza js can be found at [https://docs.cortezaproject.org/corteza-api-docs/corteza-js/{PAGE-VERSION}/index.html](https://docs.cortezaproject.org/corteza-api-docs/corteza-js/%7BPAGE-VERSION%7D/index.html).
- The API supports **pagination** using cursors.
- It also provides an SQL-like **query language** for filtering and sorting records.

**2. Authentication:**

- Corteza implements the **OAuth2** authentication protocol, acting both as an OAuth2 server and client.
- This allows both internal and external authentications.
- You can create **auth clients** in the {APP_NAME_ADMIN} panel for external applications to use for authentication.
    - It is recommended to create a separate auth client for each application you want to integrate with.
    - You can configure these auth clients in the `menu:system[auth clients]` section.
- Corteza also supports **external identity providers** that use the OpenID Connect (OIDC) protocol, such as Google, LinkedIn, and GitHub.
- You can use the `corteza-vue plugins/auth` to manage authentication for Vue-based applications.
- You can also use Corteza to authenticate other Corteza instances.
    - To do this, create a new auth client and make sure you select the `authorization_code` grant type.
    - Check the `allow client to use OIDC and verify user's identity` capability.

**3. Integration Gateway:**

- Corteza provides an **Integration Gateway** that allows you to create custom API endpoints for webhooks or other integrations.
    - These endpoints can be configured in the `menu:System[Integration Gateway]` sub-page within the admin area.
    - The integration gateway has a built-in profiler.
- The Integration Gateway is tightly integrated with the workflow engine.
- You can process requests with Javascript within the Integration Gateway.
- You can also create HTTP methods.

**4. Federation:**

- Corteza Federation enables different Corteza instances to establish a **federated network** for secure information exchange.
- This feature includes **node pairing** and **data synchronization**.
    - Node pairing involves a handshake to exchange authentication credentials securely.
    - Data synchronization includes structure and data syncing between nodes.
- Federation leverages system users and JWT tokens, using the RBAC access control system.
- You can use the `corteza-server sync data` and `corteza-server sync structure` commands to force the background watcher to run.
- Corteza does not import Federation roles and RBAC rules when upgrading existing databases; this needs to be done manually.

**5. Messagebus:**

- Corteza's **message bus** allows you to offload work from a producer instance to a consumer instance via message queues.
- It's primarily designed for use with workflows, but it can be extended to work elsewhere.
- The sink processor constructs the proper response (headers and body) based on the request.

**6. Automation and Workflows:**

- Corteza allows you to automate tasks using **workflows** and **automation scripts**.
    - Workflows are visual and can execute automation scripts.
    - The automation system can trigger events when resources are created, updated, deleted, or when users log in.
    - Workflows can interact with the RBAC facility.
    - Workflows can also be used to interact with the message bus.
- Automation scripts can return full response objects (body, headers) on sink requests.

**7. Other Integration Options**

- You can integrate with Nylas for email, calendar, and contact provider.
- You can create custom API endpoints for webhooks or custom integrations, tightly integrated with workflows for request processing.

By using these features, you can effectively integrate Corteza with various other applications, tailoring the integration to meet your specific requirements. You can use the API for basic interactions, the authentication mechanisms for secure access, the Integration Gateway for custom endpoints, Federation for data sharing, and the automation features to define complex business logic.                                                                     
""")

st.expander("4 - How does Corteza Integration Gateway work?", expanded=False).markdown("""
The Corteza Integration Gateway allows you to create **custom API endpoints** that can support custom authentication methods, request validation, and rate limiting. It serves as an alternative to sink endpoints and is tightly integrated with the Corteza workflow engine.

Here's a breakdown of how the Integration Gateway works, based on the sources:

**1. Purpose and Functionality:**

- The Integration Gateway allows you to define **custom API endpoints** for incoming webhooks, processing data from external integrations, or proxying requests to other services.
- It simplifies the development and troubleshooting process, allowing you to inspect particular requests in detail.
- The gateway can also be used to benchmark system performance.

**2. Configuration:**

- You can create and manage Integration Gateway endpoints in the **admin area** of your Corteza instance under `menu:System[Integration Gateway]`.
- When creating an endpoint, you define:
    - The **path** for the endpoint.
    - The **HTTP method** for the endpoint.
- Endpoints are accessed via the URL `$BASE_URL/api/gateway/$YOUR_ENDPOINT`.
- You can define different HTTP methods on the same route but they must be specified as different endpoints.
- You can set up filters to pre-process incoming requests.
    - One example of a prefilter is setting a header token.

**3. Request Processing:**

- The Integration Gateway supports several built-in processors.
- For more advanced operations, you can use:
    - **JavaScript code snippets**.
        - The input object parameters are the HTTP request object and the Integration Gateway configuration.
    - **Workflows**.
        - You can bind a workflow to the endpoint to handle requests.
        - The workflow will inherit the invoking user's permissions.
        - The workflow receives the request payload and can process it using various workflow steps.
        - Within a workflow, the request body can be read using the `readRequestBody(input)` function, and parsed using `JSON.parse()`.

**4. Workflow Integration:**

- To bind a workflow to an endpoint:
    - Create a new or edit an existing Integration Gateway endpoint.
    - Add a **workflow processer** to the endpoint.
    - Select the desired workflow from the dropdown menu.
- Workflows can be used to send data to external services.

**5. Response Generation**

- The sink processor within the message bus constructs the proper response (headers and body) based on the request.
- Responses can be configured as a default JSON response.

**6. Profiling:**

- The Integration Gateway includes a **route profiler** to inspect requests.
    - It allows you to benchmark system performance and identify potential bottlenecks.
    - The profiler can be enabled via the web interface or through the system settings.
    - The profiler displays a list of all logged requests for a specific route.
    - The profiler's data is not stored and will be reset on server restart.

**7. Testing:**

- You can use tools like Postman or cURL to test Integration Gateway routes.

In summary, the Corteza Integration Gateway acts as a flexible interface to create custom API endpoints, process requests with JavaScript or workflows, and integrate with other systems, making it a powerful tool for building custom integrations.                                                                           
""")

st.expander("5 - How to create a Corteza workflow?", expanded=False).markdown("""
To create a Corteza workflow, you'll use the workflow editor within the Corteza platform. Here's a step-by-step guide based on the provided sources:

**1. Access the Workflow Application:**

- Navigate to your Corteza instance (e.g., `http://latest.cortezaproject.org/`).
- Click on the **"Workflows" application**.

**2. Create a New Workflow:**

- Click on the **"New Workflow" button**. This will open a modal window where you'll define the initial workflow parameters.
- Fill in the required fields:
    - **Label**: A user-friendly name for the workflow (e.g., "My Test Workflow").
    - **Handle**: A unique value for referencing the workflow. Handles must be unique and can contain lowercase letters, numbers, and hyphens.
    - **Description**: A detailed explanation of what the workflow does.
    - **Run as**: Defines which user's permissions the workflow will use during execution.

**3. Workflow Editor Interface:**

- The workflow editor has four main parts:
    - **Workflow Configuration Screen**: Accessed via the gear icon {ICON_WORKFLOW_COG} in the header, for basic workflow settings.
    - **Toolbar**: Contains all the available workflow steps that you can drag and drop onto the canvas.
    - **Canvas**: The main area where you build and configure the workflow.
    - **Step Configurator**: Where you configure individual workflow steps.

**4. Structuring the Workflow:**

- **Add Steps**: Drag and drop steps from the toolbar to the canvas to build the workflow.
- **Connect Steps**: Draw connectors between the steps to define the flow of the workflow.
    - Click a connector to view its connection points.
    - Drag a connection point to change the start or end of the connector.
- **Use Copy-Paste**: Use `cmd+c` and `cmd+v` to duplicate existing steps.
- You can use the right mouse button to pan the canvas, and the scroll wheel to zoom.

**5. Configure Workflow Steps:**

- To configure a specific step, click on the configuration icon {ICON_WORKFLOW_COG} in the step header.
- The configuration is saved automatically to the step, but you must save the workflow for changes to take effect.
- When using expressions, ensure that the passed data can change based on the workflow's scope.

**6. Key Workflow Elements:**

- **Triggers:** Every workflow must start with a trigger {ICON_WORKFLOW_TRIGGER}.
- **Termination Step**: A termination step {ICON_WORKFLOW_TERMINATION} is optional, but can increase clarity. A workflow can have multiple triggers and termination steps.
- **Iterators:** Use iterators {ICON_WORKFLOW_ITERATOR} to process multiple items sequentially. An iterator has a configuration section and an iterator body.
- **Gateways:** Use gateways to implement conditional executions based on the workflow's state. There are three types of gateways: _exclusive_ {ICON_WORKFLOW_GATEWAYEXCLUSIVE}, _inclusive_ {ICON_WORKFLOW_GATEWAYINCLUSIVE}, and _fork_ {ICON_WORKFLOW_GATEWAYPARALLEL}.
- **Delay Step:** Use the delay step {ICON_WORKFLOW_DELAY} when you need to introduce a delay in your workflow.
- **Deferred Trigger**: Use the deferred trigger {ICON_WORKFLOW_TRIGGER} when you need to defer the execution of a workflow.
- **Prompts:** Use the prompt step {ICON_WORKFLOW_DELAY} when you need user input.

**7. Saving Your Workflow:**

- Click on the **save button** at the bottom of the screen, or use `ctrl+s`.

**8. Testing Your Workflow:**

- Click the play icon {ICON_WORKFLOW_PLAY} on the trigger to test your workflow.
- A pop-up will ask for the initial scope, which is the data passed to the workflow when it is executed.
- Enter the required parameters for the initial scope and click the **"Load and Configure"** button.
- If there are missing parameters, they will be automatically added with an empty value for the type.
- Click the **"Run Workflow"** button to test it or **"Back"** to go back to the previous screen.

**9. Important Considerations:**

- All data in the workflow is typed.
- Subworkflows cannot utilize triggers and cannot be executed like regular workflows.
- When using a delay or prompt step, the workflow becomes asynchronous and cannot invalidate actions like record creation, updates or deletes.

By following these steps, you can create and configure workflows in Corteza to automate your business processes. Remember to configure each step properly according to its purpose and connect them logically to achieve the desired workflow behavior.
""")

st.expander("6 - What endpoint is used to add a record?", expanded=False).markdown("""
To add a record in Corteza, you would use a **POST** request to the appropriate API endpoint. Here's a breakdown of the relevant information:

- **Endpoint Structure:** The base URL for the API request is structured as follows: `$BASE_URL/api/compose/namespace/$NAMESPACE_ID/module/$MODULE_ID/record/`.
    
    - `$BASE_URL` is the URL to your Corteza instance.
    - `$NAMESPACE_ID` is the identifier of the namespace where the record will be created.
    - `$MODULE_ID` is the identifier of the module to which the record will belong.
- **Request Method:** The HTTP method used to create a record is **POST**.
    
- **Authentication:** You must include an authorization header with a valid JWT (JSON Web Token). This is typically included as: `-H "authorization: Bearer $JWT"`.
    
- **Content Type:** The request must specify a `content-type` of `application/json`. This is typically included as `-H 'content-type: application/json'`.
    
- **Request Body:** The body of the POST request must include the data for the new record in JSON format. This data is organized as a JSON object with a `values` array.
    
    - Each object in the `values` array has a `name` and `value`. The `name` is the field name from the module.
    - Example request body to create a record:
        
        ```
        {
          "values": [
             { "name": "f1", "value": "value 1" },
              { "name": "f2", "value": "value 2" }
            ]
        }
        ```
        
    - If you want to create multiple records in a single request, you can use the bulk endpoint by providing a `records` array.
- **Example `curl` command to add a single record:**
    
    ```
    curl -X POST "$BASE_URL/api/compose/namespace/$NAMESPACE_ID/module/$MODULE_ID/record/" -H 'accept: application/json, text/plain,  */*' -H "authorization: Bearer $JWT" -H 'content-type: application/json' --data-raw '{ "values": [{ "name": "f1", "value": "value 1" },{ "name": "f2", "value": "value 2" }]}' --compressed
    ```
    
- **Example `curl` command to add multiple records:**
    
    ```
        curl -X POST "$BASE_URL/api/compose/namespace/$NAMESPACE_ID/module/$MODULE_ID/record/" -H 'accept: application/json, text/plain,  */*' -H "authorization: Bearer $JWT" -H 'content-type: application/json' --data-raw '{"records": [{"set": [{"values":[{"name":"f1","value":"a"},{"name":"f1","value":"b"}]},{"values":[{"name":"f1","value":"a"},{"name":"f1","value":"b"}]}]}]}' --compressed
    ```
    
- **Response:** A successful request will return a JSON response that includes the `recordID`, `moduleID`, and the created record values.
    
    ```
        {"response": {"recordID": "RECORD_ID","moduleID": "MODULE_ID","values": [{ "name": "f1", "value": "value 1" },{ "name": "f2", "value": "value 2" }],"namespaceID": "NAMESPACE_ID"}}
    ```
    

In summary, to add a record to a Corteza module, send a POST request to the specified endpoint with the necessary authentication and data in the request body.
""")

st.expander("7 - How to create a workflow step to read the request body from the integrated gateway?", expanded=False).markdown("""
To create a workflow step that reads the request body from the Integration Gateway, you can use the **"Process arbitrary data in jsenv"** function step. This step allows you to execute JavaScript code that can read and process the request body. Here's how to configure it:

- **Add a "Process arbitrary data in jsenv" step** to your workflow.
- **Configure the step**:
    - Set the `source` argument to a JavaScript code snippet that reads the request body. You can use the **`readRequestBody(input)`** function for this purpose. The `input` variable is of type HttpRequest. The function returns the body of the request as a string.
        
        - For example: `readRequestBody(input.Get('request'))`
    - Set the `scope` argument to `payload`. This will provide the request payload as input for the Javascript code.
        
    - Use the `resultAny` argument to store the parsed payload. This will store the output of the javascript code in a workflow variable, for example, set `resultAny` to `parsedPayload` to store the output in the `parsedPayload` variable.
        
    - Example:
        
        ```
        try {
          return JSON.parse(readRequestBody(input));
        } catch (e) {
          return 'could not parse request body: ' + e.message
        }
        ```
        
        This code snippet attempts to parse the request body as JSON. If parsing fails, it returns an error message.
        
- **Use the parsed payload**: After this step, you can access the parsed payload (in this example in the `parsedPayload` variable) in subsequent steps in your workflow.

**Important considerations**:

- **Integration Gateway Setup:** Make sure that the workflow is triggered by the Integration Gateway. This is done by configuring the workflow to have a trigger with the `System` resource and the `onManual` event. The Integration Gateway endpoint should be configured with a **workflow processer** that calls this workflow.
- **Request Content-Type**: The above JavaScript example shows how to parse the request as JSON. If you expect a different content type (e.g. plain text, form data), you'll need to adjust the parsing logic accordingly.
- **Error Handling**: The provided JavaScript snippet includes basic error handling, but you may want to add more robust error handling to manage different scenarios when reading the request body.
- **Alternative**: Another approach is to use the `apigwBody` function to read the request body from the integration gateway, but this does not include parsing of the request body.

**Example workflow** Here is a summary of a workflow that reads the request body from the integrated gateway.

1. A **System; onManual** trigger.
2. A **Process arbitrary data in jsenv** function step:

- The `scope` argument is set to `payload`.
- The `source` argument contains the javascript code to read the request body.
- The `results` argument is set to a variable, for example, `parsedPayload`.

3. A **Debug state** step to inspect the state of the workflow after reading the request body.
4. A **Done** step.

By using these steps, you can successfully read and process the request body from an Integration Gateway endpoint within a Corteza workflow, allowing you to perform various operations on the data received.
""")

st.expander("8 - How to create a workflow step to send an HTTP request to a webhook address. For example, with the webhook address: https://webhook.site/{webhookId}/", expanded=False).markdown("""
To create a workflow step that sends an HTTP request to a webhook address, you can use the **`httpRequest`** function step. Here's how to configure it:

- **Add a function step** to your workflow.
- **Configure the function step**:
    - Set the `type` to **`httpRequest`**.
    - Set the `url` parameter to the webhook address (e.g., `https://webhook.site/{webhookId}`). You can use a string literal or an expression to dynamically set the URL.
    - Set the `method` parameter to the HTTP method you want to use (e.g., `POST`, `GET`, `PUT`). Use a string literal or an expression.
    - You can configure other optional parameters, including:
        - `params` (KVV): URL query parameters.
        - `headers` (KVV): HTTP headers.
        - `headerAuthBearer` (String): Authentication token.
        - `headerAuthUsername` (String): Username for authentication.
        - `headerAuthPassword` (String): Password for authentication.
        - `headerUserAgent` (String): User agent string.
        - `headerContentType` (String): Content type of the request.
        - `timeout` (Duration): Request timeout duration.
        - `form` (KVV): Form data for a `POST` request.
        - `body` (String, Reader, Any): Request body. This can be a string, an `io.Reader`, or any other type. You can use an expression to set the body to a stringified JSON, for example: `toJSON(myPayload)`.

**Example:** To send a `POST` request with a JSON body to the webhook address, you could configure the `httpRequest` step like this:

- `url`: `https://webhook.site/{webhookId}`
- `method`: `POST`
- `headers`: Set the `Content-Type` header to `application/json`, for example: `{ "Content-Type": ["application/json"] }`
- `body`: Use an expression to convert a payload variable to a JSON string, for example `toJSON(myPayload)`. You can use a workflow expression step to define the `myPayload` variable.

**Important considerations:**

- **Workflow trigger**: Ensure your workflow has a trigger that starts the execution. For example, an `onManual` trigger allows you to manually test the workflow, and triggers from other events, such as record updates or time intervals, can be used to trigger the workflow automatically.
- **Error handling**: You should consider how your workflow should handle HTTP request errors. You can use an error step to manually trigger an error, which can prevent additional operations from executing if the request fails.
- **Data formatting**: You will likely need to format the data you are sending to the webhook, and this can be done using a Javascript step or workflow expressions before sending the HTTP request. For example, you can use an expression step to convert the data to JSON, before passing it to the http request step.
- **Security**: If your webhook requires authentication, you should use the `headerAuthBearer`, `headerAuthUsername`, or `headerAuthPassword` parameters to provide credentials.
- **Logging**: Use the debug step or workflow logging functions to log relevant information about the HTTP request, such as the URL, the method, the headers, the body, and the response. This can help you troubleshoot issues. You can also use the Integration Gateway profiler to view the requests if the webhook is routed through the gateway.
- **Testing**: Use the workflow test feature to test the workflow. You can run the workflow manually, providing initial values and check how the execution path behaves with the given input.

By configuring the `httpRequest` function step with the appropriate parameters, you can send HTTP requests to webhook addresses, and integrate Corteza with other services.
""")