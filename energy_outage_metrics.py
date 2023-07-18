# Methods for measuring energy outages

def SAIDI(avg_min_nopower: float, total_customers: int, total_customers_nopower: int) -> float:
    """
    Calculates the System Average Interruption Duration Index (SAIDI).

    SAIDI is calculated by multiplying the average duration of customer interruptions by their total number
    and then dividing by the total number of customers in the system.

    Args:
        avg_min_nopower (float): Average duration of customer interruptions in minutes.
        total_customers (int): Total number of customers in the system.
        total_customers_nopower (int): Total number of customers experiencing power interruptions.

    Returns:
        float: SAIDI value representing the total duration of average customer interruption.

    """
    return (avg_min_nopower * total_customers_nopower) / total_customers


def SAIFI(total_customers_nopower: int, total_customers: int) -> float:
    """
    Calculates the System Average Interruption Frequency Index (SAIFI).

    SAIFI is calculated by dividing the total number of customers interrupted by an outage
    by the total number of customers in the system.

    Args:
        total_customers_nopower (int): Total number of customers experiencing power interruptions.
        total_customers (int): Total number of customers in the system.

    Returns:
        float: SAIFI value representing how often the average customer experiences an interruption.

    """
    return total_customers_nopower / total_customers


def CAIDI(total_min_outages, total_customers) -> float:
    """
    Calculates the Customer Average Interruption Duration Index (CAIDI).

    CAIDI is calculated as the total minutes of customer interruption divided by the total number
    of customers interrupted.

    Args:
        total_min_outages (float): Total minutes of customer interruption.
        total_customers (int): Total number of customers interrupted.

    Returns:
        float: CAIDI value representing the average time required to restore service.

    """
    return total_min_outages / total_customers


def CAIFI(count_outages, total_customers_nopower) -> float:
    """
    Calculates the Customer Average Interruption Frequency Index (CAIFI).

    CAIFI is calculated by dividing the number of interruptions by the number of customers experiencing
    interruptions.

    Args:
        count_outages (int): Total number of interruptions.
        total_customers_nopower (int): Total number of customers experiencing power interruptions.

    Returns:
        float: CAIFI value representing the number of interruptions each impacted customer experiences.

    """
    return count_outages / total_customers_nopower
