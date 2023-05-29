document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("story-form");
  const storyDisplay = document.getElementById("story-display");
  const generatedStories = document.getElementById("generated-stories");
  const storyBoxes = document.getElementsByClassName("story-box");
  const expandedStory = document.getElementById("expanded-story");
  const backButton = document.getElementById("back-button");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    // Collect form data
    const formData = new FormData(form);
    const requestData = Object.fromEntries(formData.entries());

    // Send the data to the server
    fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Display the generated stories
        displayStories(data.stories);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  backButton.addEventListener("click", () => {
    hideExpandedStory();
  });

  function displayStories(stories) {
    // Clear the existing stories
    generatedStories.innerHTML = "";

    // Create story elements
    for (let i = 0; i < storyBoxes.length; i++) {
      const storyBox = storyBoxes[i];
      const story = stories[i];

      storyBox.addEventListener("click", () => {
        showExpandedStory(story);
      });

      generatedStories.appendChild(storyBox);
    }

    // Show the story display section
    storyDisplay.style.display = "block";

    // Scroll to the story display section
    storyDisplay.scrollIntoView({ behavior: "smooth" });
  }

  function showExpandedStory(story) {
    expandedStory.textContent = story;
    storyDisplay.style.display = "none";
    expandedStory.style.display = "block";
    backButton.style.display = "block";
  }

  function hideExpandedStory() {
    expandedStory.textContent = "";
    expandedStory.style.display = "none";
    backButton.style.display = "none";
    storyDisplay.style.display = "block";
  }
});
