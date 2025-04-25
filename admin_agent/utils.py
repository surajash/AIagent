def generate_suggestions(metrics):
    return [f"Check high usage in metric {i+1}" for i, value in enumerate(metrics) if value > 80]