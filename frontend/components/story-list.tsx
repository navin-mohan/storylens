import Link from "next/link"
import type { Story } from "@/lib/types"

interface StoryListProps {
  stories: Story[]
}

export default function StoryList({ stories }: StoryListProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {stories.map((story) => (
        <Link key={story.id} href={`/story/${story.id}`}>
          <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow cursor-pointer h-full">
            <div className="p-6">
              <h2 className="text-xl font-bold mb-2 line-clamp-2">{story.title}</h2>
              <p className="text-gray-600 text-sm mb-4">By {story.author}</p>
              <p className="text-gray-700  mb-4">{story.summary}</p>
              <p className="text-blue-600 text-sm">Read more →</p>
            </div>
          </div>
        </Link>
      ))}
    </div>
  )
}
