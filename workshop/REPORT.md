# Workshop Report

We conducted a two-stage workshop to introduce our fairness monitoring tool to participants and understand their challenges in implementing fairness practices in an industry setting.

**Session 1** (Wednesday, 5th February 2025): Methods for identifying harmful biases throughout the AI development process, using the existing system cards with the FAID tool to monitor fairness. This session also featured real-world case studies from the finance sector, highlighted potential applications in other industries, and offered practical recommendations for integrating fairness into AI systems.

**Session 2** (Thursday, 6th March 2025): Collecting feedback and assessing the effectiveness of adoption of the toolkit in SME development context 

The workshop steered our research and development by highlighting key industry concerns, evolving needs, and the priorities of organizations of different sizes.

## Session I

In the first session, we had 11 participants with diverse technical expertise. All were professionals with technical backgrounds but at different career stages, including technical product managers, machine learning engineers, data scientists, R&D professionals, as well as directors and managers. 

We began with an introduction to fairness in AI and the key characteristics of trustworthy AI since our participants came from the industry and had limited experience with fairness studies. Throughout the workshop, participants worked on a use case, either a real-world application or a relevant theoretical scenario. 

> See the [Presentation PDF](https://github.com/alan-turing-institute/fairness-monitoring/blob/main/workshop/workshop.pdf).

- **Defining the use case:** The first activity focused on defining a use case by identifying three key components: (1) ML Task: Classification, regression, or generation  (2) Model Type: Shallow or deep learning  (3) Potential Data Sources: Tabular, image, audio, text, etc.  
- **Understanding bias and regulatory context:** Next, we introduced protected characteristics and how current regulations address fairness in ML model development. Using insights from the recent International AI Safety Report, we demonstrated different bias types, including: Sampling bias, selection bias, historical bias, labeller bias, evaluation bias, and feedback loop bias.
- **Identifying bias with bias type cards:** Participants then used Bias Type Cards. Each card featured the bias name and a brief description, as well as a more detailed explanation with speculative prompts to help identify the bias. Participants selected the most relevant biases for their use cases and mapped them to specific ML lifecycle stages where developers and stakeholders should be particularly vigilant.  
> [Bias Cards](https://github.com/alan-turing-institute/turing-commons/blob/resources/resources/activities/bias-and-mitigation-cards.pdf) is another project output of the Alan Turing Institute.
- **Existing metadata in AI development - Intro:** We introduced our workflow, focusing on metadata management and technical considerations. Participants explored how existing metadata could be leveraged to monitor potential biases across different ML stages.
- **Group work for monitoring fairness using metadata:** In the final interactive activity, participants selected relevant data, model components, and fairness log entities to form “monitoring groups.” These groups were designed to proactively track values and detect potential bias-related risks.

At the end of the session, each group presented their work and provided feedback to one another. 

## Session II

In this session, we conducted a more focused discussion with selected individuals from different industries that participated in the previous session. The main goal of the session was to gather feedback on the resources and how they are being integrated into real-world solutions, as well as the challenges encountered.

> See the question set we used in this session: [Fairness Implementation Question Set](./FCONSIDERATIONS.md)


## Workshop Findings

In the first session, observations from interactive activities and discussions led to product-focused insights. The second session focused on organisational implementation, skill development, and future directions.
 
### Fairness Management Flow

In the workshop, we observed that, our current approach of fairness management flow is quickly learnable and implementable: 

<table><td>Identify use case and context ➡️ Discuss potential bias and harms ➡️ Define safety requirements in the requirement planning stage ➡️ Learn fairness ontology and construct knowledge graphs ➡️ Review metadata and map bias-monitoring options</td></table>

- This proactive methodology supported bias identification and governance integration in theoretical use cases. However, the requirements change dramatically for different organisations. **Action:** _We are structuring the FAID repository to present itself as an overall methodology with a structured set of functions rather than just a standalone tool to allow this customisability and support developers in their high-level decision making._  
- Further, we identified a need for UML-like diagrams to encapsulate governance and safety considerations for achieving trustworthy AI systems. **Action:** _Existing frameworks could be integrated into visual governance flows with clear enterprise-level software engineering links. Further, our demo tutorials are limited in conveying the capability of metadata files in AI fairness and bias monitoring._
- Participants struggled to correctly define relevant entities within the system. Providing clear definitions and explaining the origins of entities (e.g., from *Croissant* and the *Data Cards Playbook*) helped in understanding the rationale behind certain metadata metrics. ** Action:**  _Link common metadata formats to the FAID format._

### Comprehensive and Transferable Use Cases

- Participants raised important questions about **data and model versioning** in AI governance. **Action:** Exploring tools such as **DVC (Data Version Control)** and **CMF (Configuration Management Frameworks)** could help assess their strengths and limitations for tracking AI model evolution.  
- There is a clear need for comprehensive, transferable examples. Participants require **good end-to-end examples** of AI fairness workflows. Most existing AI fairness materials share the same foundational content, yet practitioners struggle to apply this knowledge across different contexts. **Action:** Develop well-structured tutorials with enterprise-level examples that can be translated easily to new enterprise-level use cases.


### Challenges in Adoption and Integration of AI Fairness

- The meeting highlighted the subjective nature of fairness and the difficulty in defining universal metrics and acceptable levels of bias. The concept of fairness often involves trade-offs, particularly with model accuracy. The discussion touched upon balancing commercial objectives with fairness considerations.
- Participants from both small and large size organisation highlighted the difficulties in gaining buy-in for AI fairness initiatives within their companies. For all companies, it is challenging to demonstrate the value of implementing a fairness-oriented approach. For larger companies, it is challenging to change/update the existing ethical principles and responsibility practices. Time constraints and prioritisation were also noted as hurdles. **Action:** _Choosing the right interpretability method can actually help organisations to visualise the harmful use cases and create some value in the decision-making process. However, it is also challenging to pick the right techniques for the given model and data. Further, most interpretability techniques are starting points rather than final outputs due to their local approximation nature._
- The discussion revealed different approaches to AI fairness based on the industry and the perceived risk of AI applications. Smaller organisations tend to think more proactively about fairness. However, larger organisations, while having guidelines and prioritising fairness as a principle, found it challenging to implement concrete tests due to a lack of access to sensitive data like gender and ethnicity (partly due to GDPR). Their focus was more on high-level fairness considerations and ensuring it's "business as usual". Based on sectoral regulations, larger organisations currently explore different fairness evaluation techniques in the model validation stage of their lifecycle. **Action:** _The need to raise literacy around AI fairness and the trade-offs involved was emphasized in the meeting. Developing a complete, easily-understandable guidance with clear guidelines and policies (potentially drawing inspiration from regulations like GDPR and the upcoming EU AI Act) for the use of management level is required._
- Measuring the success of responsible AI efforts is challenging but can involve qualitative assessments of internal discussions and action plans, as well as considering client feedback and the alignment with company values. Demonstrating use cases that are both profitable and fair is seen as a key goal. The increasing demand from clients for fair and explainable AI models is also driving the need for these practices.


## Participant Profile

**Their current use and sectoral perspective of AI:** They reported involvement in a diverse range of ML/AI development efforts, including healthcare applications, information processing, broader consultation on model evaluation and governance, and infrastructure and data management. We also asked the question to understand their sectoral perspectives on AI development and their motivation in participating in the workshop. They highlighted the following \textit{short-term trends:} The adoption of LLMs for their existing business applications. Enhanced efficiency through AI-driven automation in workflows. Integration of LLMs into everyday tasks, including search, information retrieval, and translation. Improved cost-benefit analysis of machine learning (ML) versus traditional approaches.And, some of the \textit{long-term trends} they identified are: Evolution toward agentic AI systems capable of autonomously executing user-defined tasks. Increasing AI independence in handling complex, non-human-performable tasks. Seamless ML integration with minimal additional burden on developers. Development of standardised and trusted metrics for LLM fairness. Growing emphasis on trust and transparency in AI implementation.  

These trends indicate that they have already received requests from their clients or companies to integrate AI into their current products/services. But, they are still struggling in the assessment of these products using reliable and robust metrics.

**Their challenges:** Workshop participants identified several major challenges in AI development, including:  Difficulty in keeping up with fast-moving innovations and evolving AI capabilities.  Challenges in sourcing, cleaning, and maintaining high-quality data for AI models.  
Ensuring comprehensive assessment of LLMs and AI systems throughout their lifecycle.  
Balancing speed of iteration from prototype to production while maintaining robust evaluation. High costs associated with training, processing, storage, and clinical trials.  Selecting appropriate vendors and integrating AI systems effectively.  

**The main barriers for them to the responsible adoption and use of AI systems:** Difficulty in understanding AI metrics, selecting safe and ethical solutions, and developing an AI strategy that ensures responsible use. Lack of support from management and concerns about integrating AI responsibly within business operations. Ambiguity around legal and ethical boundaries, particularly regarding data privacy and compliance. Poor data governance structures, limited access to key data (e.g., protected characteristics), and over-reliance on third-party systems with opaque decision-making ("black boxes").  High costs of AI infrastructure, limited innovation capacity, and difficulty in attracting AI talent. Startups and smaller firms face pressure to iterate quickly, often without sufficient time to assess the full impact of AI decisions.  

When we talk about fairness as a trustworthiness component, the conversation is structured around transparency. They emphasised the need for an interpretable mechanism with clear decision-making processes. 

**Top ask of policy-makers:** Regulations should consider the entire AI value chain, including environmental impacts.  AI policies should be concise, easy to understand, and available in summarisable formats. Provide worked examples and gold-standard deliverables to help organisations comply effectively.

