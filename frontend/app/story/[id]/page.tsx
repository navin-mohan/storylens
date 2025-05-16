"use client"

import { Navbar } from "@/components/navbar"
import { useParams } from "next/navigation"
import { useEffect, useState } from "react"
import { getStory } from "@/lib/data"

export default function StoryPage() {
  const params = useParams()
  const storyId = params.id as string

  const [story, setStory] = useState(null)
  useEffect(() => {
    getStory(storyId).then(
      story => setStory(story)
    )
  }, [])

  if (!story) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <div className="container mx-auto px-4 py-8">
          <h1 className="text-3xl font-bold mb-8">Story not found</h1>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="container mx-auto px-4 py-8 max-w-3xl">
        <article className="bg-white p-8 rounded-lg shadow-md">
          <h1 className="text-4xl font-bold mb-4">{story.title}</h1>
          <p className="text-gray-600 mb-8">By {story.author}</p>
          <div className="prose max-w-none">
            {story.story.split("\n\n").map((paragraph, index) => (
              <p key={index} className="mb-4">
                {paragraph}
              </p>
            ))}
          </div>
        </article>
      </div>
    </div>
  )
}
