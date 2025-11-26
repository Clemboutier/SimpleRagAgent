from flow import offline_flow, online_flow

def run_rag_demo():
    """
    Run a demonstration of the RAG system.
    
    This function:
    1. Indexes a set of sample documents (offline flow)
    2. Prompts the user for a query via the CLI
    3. Retrieves the most relevant document (online flow)
    4. Generates an answer using an LLM
    """

    # Sample texts - specialized/fictional content that benefits from RAG
    texts = [
        
        # Endurance sports training
        """Training for endurance sports requires a balance of low-intensity volume and controlled high-intensity sessions. 
        The foundation comes from consistent aerobic work at moderate heart rates, which improves fat utilization, mitochondrial density, and overall durability. 
        High-intensity intervals are added sparingly to increase lactate threshold and peak power, but they must be timed around recovery and stress levels to avoid chronic fatigue. 
        Strength training supports the process by improving neuromuscular efficiency and reducing injury risk. Effective plans adjust weekly load based on heart rate, perceived exertion, and recovery markers rather than rigid mileage targets.""",
        
        # Long-Term Endurance Development
        """Long-term endurance development depends on gradually increasing training load while maintaining stable recovery patterns. 
        Athletes respond best when weekly volume grows in small increments, allowing the cardiovascular system, musculoskeletal structures, and autonomic nervous system to adapt without excessive strain. 
        Monitoring sleep quality, resting heart rate, and variability trends helps identify early signs of overload. 
        When these signals indicate stress, reducing intensity or shortening workouts prevents the accumulation of fatigue that can limit progress.""",

        # Using Training Zones Effectively
        """Structured training zones help organize workouts and ensure that each session has a clear physiological purpose. 
        Lower zones target aerobic efficiency and metabolic stability, while higher zones focus on improving oxygen delivery, lactate clearance, and anaerobic capacity. 
        Effective athletes spend most of their time in low-intensity zones, saving harder efforts for specific days where quality can be maintained. 
        This approach increases consistency and reduces the risk of burnout or injury.""",

        # Role of Strength Training in Endurance Sports
        """Strength training complements endurance work by improving functional movement patterns, joint stability, and force production. 
        Compound exercises such as squats, deadlifts, and presses build resilience in the muscles and connective tissues that support sustained efforts on the bike or while running. 
        Moderate loads with controlled repetitions are typically sufficient for endurance athletes, as the goal is durability rather than maximal strength. 
        Integrating strength sessions on days with lower endurance demand helps avoid interference and supports long-term performance gains.""",
    ]
    
    print("=" * 50)
    print("Simple RAG Agent about endurance sports")
    print("=" * 50)
    
    # Prompt the user for a query
    query = input("Ask me anything about endurance sports. ").strip()
    if not query:
        print("No query provided. Exiting.")
        return
    
    # Single shared store for both flows
    shared = {
        "texts": texts,
        "embeddings": None,
        "index": None,
        "query": query,
        "query_embedding": None,
        "retrieved_document": None,
        "generated_answer": None
    }
    
    # Initialize and run the offline flow (document indexing)
    offline_flow.run(shared)
    
    # Run the online flow to retrieve the most relevant document and generate an answer
    online_flow.run(shared)


if __name__ == "__main__":
    run_rag_demo()