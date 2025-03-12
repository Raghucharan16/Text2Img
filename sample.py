from diffusers import DiffusionPipeline

# pipe = DiffusionPipeline.from_pretrained("Lightricks/LTX-Video")
pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")


prompt = "In the epic Mahabharata, Arjuna is described as a tall, dark, and exceedingly handsome warrior, possessing curly locks, a broad chest, and long arms, known for his skill with a bow and arrows.  Here's a more detailed look at Arjuna's physical description from the Mahabharata: Height and Build: Arjuna is depicted as tall, though shorter than his brother Bhima by a span of a thumb. He is described as having a broad chest and long arms.  Complexion and Features: Arjuna has dark skin, and some depictions also refer to him as having a burnished copper eye color. He also has curly locks.  Skills and Abilities: Arjuna is a skilled archer, capable of using powerful bows like Gandiva and shooting arrows with great speed and accuracy. He is also agile and can perform complex movements, such as dancing, with ease.  Other Notable Characteristics: He is known for his determination, skill, and his fierce expression on the battlefield.  Depiction: Arjuna is generally depicted in profile with a determined, even fierce, expression on his face. He is often depicted with a golden crown or a corolla of gold. His dark face often sports a moustache. "
image = pipe(prompt).images[0]
image.save("arjuna_image.png")  # Save the image to a file
# image.show()  # Uncomment this if you want to display it (works in some environments)