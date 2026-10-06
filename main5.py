import logging

logging.basicConfig(level=logging.INFO)

logging.info("Симуляція почалася")

for i in range(5):
    print("Хід симуляції", i + 1)
    logging.info("Виконано хід симуляції")

logging.info("Симуляція завершилася")