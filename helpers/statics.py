weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
project_names = ['struts-sandbox', 'tez', 'commons-beanutils', 'druid', 'incubator-datasketches-java',
                 'netbeans-mavenutils-nbm-maven-plugin', 'maven-archetype', 'sling-org-apache-sling-resourceresolver',
                 'sling-whiteboard', 'incubator-druid', 'commons-codec', 'incubator-taverna-workbench', 'commons-exec',
                 'qpid-jms-amqp-0-x', 'vxquery', 'maven-wagon', 'karaf-cellar', 'camel-spring-boot', 'synapse', 'tomee',
                 'commons-csv', 'commons-math', 'incubator-brooklyn', 'maven', 'incubator-hivemall',
                 'phoenix', 'incubator-tamaya', 'crunch', 'jclouds-labs', 'brooklyn-library', 'myfaces', 'mahout',
                 'empire-db', 'juddi', 'roller', 'tinkerpop', 'opennlp', 'servicecomb-java-chassis',
                 'httpcomponents-core', 'hadoop-ozone', 'xalan-java', 'flink', 'myfaces-trinidad',
                 'maven-dependency-plugin', 'mina-sshd', 'helix', 'incubator-iotdb', 'cxf', 'shiro', 'jclouds',
                 'sling-org-apache-sling-starter', 'apex-malhar', 'apex-core', 'maven-plugin-tools',
                 'incubator-shardingsphere', 'oodt', 'directory-kerby', 'attic-onami', 'incubator-dolphinscheduler',
                 'bval', 'myfaces-extcdi', 'cxf-fediz', 'calcite-avatica', 'karaf-jclouds', 'mina-ftpserver',
                 'activemq-artemis', 'incubator-taverna-language', 'marmotta', 'sling-org-apache-sling-engine',
                 'incubator-retired-wave', 'logging-log4j', 'netbeans-mavenutils-nb-repository-plugin', 'commons-scxml',
                 'samza', 'commons-fileupload', 'qpid-broker-j', 'royale-compiler', 'skywalking', 'falcon', 'hama',
                 'sling-org-apache-sling-api', 'ws-wss4j', 'commons-io', 'commons-imaging', 'attic-polygene-java',
                 'geode', 'maven-assembly-plugin', 'sling-org-apache-sling-event', 'commons-dbcp', 'activemq',
                 'servicemix-bundles', 'uima-uimaj', 'commons-configuration', 'struts', 'drill', 'incubator-pinot',
                 'incubator-shardingsphere-example', 'rocketmq', 'deltaspike', 'wicket', 'hive', 'olingo-odata4', 'sis',
                 'commons-jexl', 'aries', 'maven-javadoc-plugin', 'knox', 'sling-org-apache-sling-jcr-resource',
                 'cassandra', 'maven-release', 'directory-studio', 'sentry', 'clerezza', 'commons-pool',
                 'commons-compress', 'ant-ivy', 'jmeter', 'commons-lang', 'maven-surefire', 'openjpa', 'karaf',
                 'incubator-taverna-common-activities', 'servicecomb-pack', 'qpid-jms', 'directory-ldap-api', 'giraph',
                 'creadur-rat', 'oozie', 'commons-logging', 'mina', 'odftoolkit', 'openwebbeans', 'eagle',
                 'bookkeeper', 'asterixdb', 'camel', 'openmeetings', 'phoenix-omid', 'commons-rdf', 'nifi',
                 'netbeans-html4j', 'portals-pluto', 'commons-digester', 'accumulo', 'pulsar', 'storm', 'ode',
                 'commons-validator', 'incubator-taverna-engine', 'logging-chainsaw', 'gora', 'directory-fortress-core',
                 'maven-scm', 'unomi', 'flume', 'commons-jcs', 'commons-collections', 'commons-vfs', 'calcite', 'dubbo',
                 'karaf-eik', 'tajo', 'commons-bcel', 'systemml', 'james-project', 'db-jdo', 'nutch',
                 'httpcomponents-client', 'directory-server', 'cayenne', 'asterixdb-hyracks', 'maven-doxia',
                 'incubator-gobblin', 'parquet-mr', 'hadoop', 'brooklyn-server', 'sqoop', 'dubbo-hessian-lite',
                 'curator', 'commons-net', 'incubator-tamaya-extensions', 'fineract', 'maven-invoker-plugin',
                 'sling-ide-tooling', 'hbase', 'qpid-proton-j', 'tomcat', 'ws-axiom', 'fluo',
                 'incubator-retired-edgent', 'syncope', 'freemarker', 'maven-integration-testing', 'commons-jelly',
                 'netbeans-mavenutils-nbm-shared', 'lens']

designite_headers = ['Total LOC analyzed', 'Number of packages', 'Number of classes', 'Number of methods',
                     'Cyclic dependency', 'God component', 'Ambiguous interface', 'Feature concentration',
                     'Unstable dependency', 'Scattered functionality', 'Dense structure', 'Imperative abstraction',
                     'Multifaceted abstraction', 'Unnecessary abstraction', 'Unutilized abstraction', 'Feature envy',
                     'Deficient encapsulation', 'Unexploited encapsulation', 'Broken modularization',
                     'Cyclically-dependent modularization', 'Hub-like modularization', 'Insufficient modularization',
                     'Broken hierarchy', 'Cyclic hierarchy', 'Deep hierarchy', 'Missing hierarchy',
                     'Multipath hierarchy', 'Rebellious hierarch', 'Wide hierarchy',
                     'Abstract function call from constructor', 'Complex conditional', 'Complex method',
                     'Empty catch clause', 'Long identifier', 'Long method', 'Long parameter list', 'Long statement',
                     'Magic number', 'Missing default']

code_smell_types = ['Cyclic dependency', 'God component', 'Ambiguous interface', 'Feature concentration',
                    'Unstable dependency', 'Scattered functionality', 'Dense structure', 'Imperative abstraction',
                    'Multifaceted abstraction', 'Unnecessary abstraction', 'Unutilized abstraction', 'Feature envy',
                    'Deficient encapsulation', 'Unexploited encapsulation', 'Broken modularization',
                    'Cyclically-dependent modularization', 'Hub-like modularization', 'Insufficient modularization',
                    'Broken hierarchy', 'Cyclic hierarchy', 'Deep hierarchy', 'Missing hierarchy',
                    'Multipath hierarchy', 'Rebellious hierarch', 'Wide hierarchy',
                    'Abstract function call from constructor', 'Complex conditional', 'Complex method',
                    'Empty catch clause', 'Long identifier', 'Long method', 'Long parameter list', 'Long statement',
                    'Magic number', 'Missing default']

refactoring_types = ['Change Return Type', 'Extract And Move Method', 'Modify Class Annotation', 'Inline Variable',
                     'Change Attribute Type', 'Modify Attribute Annotation', 'Extract Superclass', 'Replace Attribute',
                     'Move Class', 'Move Attribute', 'Extract Subclass', 'Move And Inline Method', 'Move Method',
                     'Merge Attribute', 'Push Down Attribute', 'Pull Up Attribute', 'Remove Parameter',
                     'Modify Method Annotation', 'Rename Variable', 'Split Variable', 'Rename Attribute',
                     'Replace Variable With Attribute', 'Extract Class', 'Remove Variable Annotation',
                     'Add Variable Annotation', 'Move Source Folder', 'Push Down Method', 'Rename Class',
                     'Extract Attribute', 'Add Parameter Annotation', 'Add Parameter', 'Merge Variable',
                     'Split Attribute', 'Extract Interface', 'Extract Variable', 'Remove Parameter Annotation',
                     'Modify Parameter Annotation', 'Pull Up Method', 'Add Attribute Annotation', 'Rename Parameter',
                     'Split Parameter', 'Remove Method Annotation', 'Add Class Annotation', 'Extract Method',
                     'Remove Attribute Annotation', 'Change Package', 'Remove Class Annotation', 'Reorder Parameter',
                     'Move And Rename Method', 'Inline Method', 'Rename Method', 'Add Method Annotation',
                     'Change Parameter Type', 'Merge Parameter', 'Move And Rename Class', 'Move And Rename Attribute',
                     'Change Variable Type', 'Parameterize Variable', 'Modify Variable Annotation']