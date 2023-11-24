Identifying security threats in the system using logs for Penetration Testing.

Abstract:

This report talks about the importance of logs in penetration testing project focused on how logs are used for enhancing the overall security of a login system for an organization. By emphasizing the importance of logs in monitoring and analysing user activities, the project aims to provide insights into potential security threats, like unauthorized access attempts, failed login attempts and Dos attack.

In the introduction, the report talks about the increasing number of security breaches due to increasing system complexity, technological advancements, and the challenges posed by employees using personal devices. These factors underscore the critical need for robust security measures. The methodology section discusses about the tools and techniques used in the project.

The project's core work involves generating and analysing system logs to detect specific security events, such as unauthorized access attempts, and failed login attempts. Recommendations for enhancing security, including intrusion detection technologies, the principle of least privilege, and others are shown to secure the organization against evolving cyber threats.

This log detection project offers a complete structure for finding unusual activities and actions taken.
Penetration testing is a technique used to detect vulnerabilities and evaluate security threats to the system or the network. This helps the cyber team detect potential attacks, and vulnerabilities then a risk assessment is performed to see which attack has a greater risk on the system. The CIA TRIAD (Confidentiality, Integrity, and Availability) is used with the help of the GRC (Governance, Risk, and Compliance) approach to ensure the system in an organization is secure. In this report, we discuss how these tests can be collected using logs and highlight the importance of logs in the process.
Introduction:
In pen testing Logs are a crucial part in the detection of unusual activities the SANS Institute (2022), states, "System logs are the most important source of information for detecting and investigating security incidents". The number of Computer related Incidents have increased in recent years some of the factors include increasing complexity of the system, "The complexity of modern IT systems makes it increasingly difficult to manually detect security incidents. Security logs can help organizations to automate this process and identify incidents more quickly and efficiently." (Verizon, 2022). If a system becomes more complex, testing will be challenging for programmers as they must check through each layer of the system, this often leads to overlooked vulnerabilities and entry points in the code, leading to more security breaches as hackers can exploit these vulnerabilities compromising the system security. 
Additionally, as technological advancements are taking place in a very fast phase it becomes harder for security tools to keep up with these technologies. 
Another reason is that employees in an organization log in with their own devices. A survey conducted by IBM in 2023 found that 58% of organizations have experienced data breaches due to mobile devices. The survey also found that 82% of employees use their personal devices for work purposes." (IBM, 2023). this is another major concern as the individual's device could not have up-to-date software, there could be malware in their devices, or their device could be in a data breach, Employees could be a victim of phishing attacks leading to suspicious downloads in the organization’s system, making the whole organization vulnerable to an attack. So, in this report, we will focus on how logs can help detect and prevent various types of security breaches.
Significance:
The penetration testing project using logs has a high significance in this current time for protecting an organization's IT infrastructure. By aligning with the CIA Triad and integrating the Governance, Risk, and Compliance. It plays a pivotal role in detecting vulnerabilities, allowing for the prioritized mitigation of critical risks. Our report Focuses on the importance of logs in monitoring and analyzing activities, the project provides an insight of potential security threats. Recognizing the security risks associated and the importance of security. 
To do a simulated area of log generation and detection we have created a server that runs on port 9080 in the computer’s localhost. The main block diagram is given below:






Literature Review:
Log:
In computing, a log is a record of events or activities that occur within a system. These events can include user actions, system processes, error messages, security-related incidents, and more.
Logs are essential for understanding what happens in a system, diagnosing issues, and monitoring activities. "Security logs are widely used to monitor data, networks, and computer activities. By analysing them, security experts can pick out anomalies that reveal the presence of cyber-attacks or information leaks and stop them quickly before serious damage occurs." (Ricardo Ávila, 2021) They are especially crucial in the context of penetration testing to analyse and assess the security of a system or network.
Logger:
A logger, in the context of penetration testing, is a software component responsible for generating and recording log entries. It captures information about events, actions, or transactions occurring within a system or application.
Loggers are integral to security measures as they provide a detailed record of activities, which is valuable for detecting and responding to security incidents. Penetration testers may utilize loggers to simulate various attack scenarios and assess how well systems log relevant information.
Logging:
Logging refers to the process of creating and storing log entries. It involves the systematic recording of events or data in a log file for later analysis or reference.
In penetration testing, logging is crucial for evaluating the effectiveness of security controls, identifying vulnerabilities, reconstructing attack scenarios, and conducting forensic analysis. It allows penetration testers to review and interpret the recorded information to assess the security posture of a system.

This literature review explores the key aspects of penetration testing and use of logs, including its objectives, importance, contributions to enhancing cybersecurity, and future direction of penetration testing. 

Importance of logs in Penetration Testing:
Vulnerability Identification:
Penetration testing aims to uncover weaknesses in systems, networks, and applications that could be exploited by attackers.
Logs can help penetration testers identify vulnerabilities in a system by analyzing error messages, warnings, and other log entries. Unusual or unexpected log entries may indicate potential security issues.
Detection of Anomalies:
Logs capture normal system behaviors, and any deviations from these patterns can be indicative of a security issue. Penetration testers analyze logs to detect anomalies or suspicious activities that may indicate a potential security breach.
Risk Assessment:
By simulating real-world attacks and reviewing logs, penetration testers can assess the level of risk associated with different components of the system. This information helps organizations prioritize security efforts and allocate resources effectively.
Compliance Verification:
Many industries and organizations have compliance requirements that mandate the collection and retention of logs for a specific period. Penetration testers need to assess whether the logging mechanisms in place meet these compliance requirements.

Contributions to Cybersecurity:
penetration testing, when coupled with thorough log analysis, significantly contributes to cybersecurity by discovering vulnerabilities, enabling early threat detection, improving incident response capabilities, enhancing forensic analysis, validating security controls, supporting risk assessment, and ensuring compliance with industry standards. These contributions collectively bolster an organization's resilience against cyber threats.

Methodology:
For our testing and simulation, we have used various tools like,
●	Kali Linux as the main OS
●	Rsyslog/Syslog-ng for log generation
●	Flask is used as the main tool for web framework for building the web application.
●	Bash, Python, and shell for CLI, coding and scripting
●	Tools for dos attack Apache Benchmark (ab), log detection etc.
Code Overview all the steps in the code: (auth_log_simulation.py)
1.	Flask App Initialization
2.	Logging Configuration
3.	HTML Styling
4.	Global Variables
5.	log_request_info to log information about incoming requests.
6.	setting routes (index, login, get_phrase)
7.	Login Form
8.	Main Execution
Security Events and Log Entries
Accessing the webpage  
Generates this log:
 
  
Invalid login generates this log:
 
A valid login generates: a successful log. 

Authorised and Unauthorised works the same way: (Note: only admin is authorised and can only access if admin logs in first otherwise can’t access the phrase)
 

Next let’s do a Dos (Denial of Service attack) on the website:
Uses Apache Benchmark to do 50 million requests with 100 messages simultaneously.
 
  
But a script was generated for this. Which when run detects and rejects incoming traffic.
  
•	The dos_detection.sh script basically counts all the requests 1 minute form the current time. 
•	checks if number of requests is greater than 10000. 
•	if True then Rejects all requests from the Web Server.
 
Both have same number of requests, and the number of requests was less than 50 million, so the code was successful in stopping the attack.
 
Although there Is one downside because the script directly blocks all requests to the server, so accessing the website is not possible.
 
This can only be opened by the super user or admin using  
 
Then a countLogs.sh script is used for analysis to see all the logs that were generated in the last hour.
Some scripts are also used to make the simulation look more real that generates random logs. 

 
Recommendations for system improvement:
- We would like to do more scenarios like injections and other stuff to make is more
- Improve host and network security settings, such as system hardening and firewall rules.
- Frequent security audits and vulnerability assessments to detect weaknesses in the system will be better.

Conclusion:
In conclusion, this penetration testing project focusing on identifying security threats in the system using logs and has provided valuable insights in the critical role of logs in enhancing overall security. The increasing complexity of IT systems, technological advancements, and the challenges due to the usage of personal devices by employees shows the importance of robust security measures. The project gets the solution for some challenges stated in the start of this report. As the issue of complexity was solved by adding logs for accessing each part of the website. Access control measures were added so that only the authorised person can access the crucial parts of the website and the issue of employees logging from their personal devices, now the server currently runs in the machine, but we can easily change this by making it in the network.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9080)
so, all the problems which were stated are solved in this report. Additionally, a dos attack was conducted, and script was made so that the malicious attempt can be identified, and appropriate measures were also taken as the script automatically rejected requests when it detected the attempt. However, there were certain limitations, like the script blocked all requests to the server during a Dos attack. Recommendations for system improvement include conducting more scenarios, enhancing host and network security settings, and implementing frequent security audits and vulnerability assessments.

In conclusion, this penetration testing project was successful in using for detection and prevention of security breaches. And The findings and recommendations positively impact  the efforts to strengthen IT security in evolving cyber threats.
All the codes used are in the given link.
HTTPS://GITHUB.COM/YADIDIDIAH24/SECURITYPROJECTLOGS/TREE/MAIN


References:
•	SANS Institute. (2022). SANS DFIR Handbook: Security Forensics, Investigation, and Response (4th ed.). John Wiley & Sons.
•	Verizon. (2022). 2022 Verizon Data Breach Investigations Report. Verizon.
•	IBM. (2023). Cost of a Data Breach Report 2023. IBM.
•	Ávila, R. et al. (2021) Use of security logs for Data Leak Detection: A Systematic Literature Review, Security and Communication Networks.
